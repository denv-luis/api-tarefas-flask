from flask import Flask, request, jsonify, render_template

from banco import criar_tabela
from services import tarefa_service
from services import usuario_service
from flasgger import Swagger
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
# JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)
try:
    criar_tabela()
except Exception as e:
    print("Erro ao criar banco:", e)

# Swagger config
Swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs"
}
swagger_template = {
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Digite: Bearer SEU_TOKEN"
        }
    }
}
Swagger(app, config=Swagger_config, template=swagger_template)

@app.route("/")
def pagina_inicial():
    return render_template("index.html")


# LISTAR TAREFAS
@app.route("/tarefas", methods=["GET"])
@jwt_required()
def listar():
    """
    ---
    security:
      - Bearer: []
    responses:
      200:
        description: Listar tarefas
    """
    usuario_id = int(get_jwt_identity())
    tarefas = tarefa_service.listar_tarefas(usuario_id)

    return jsonify({
        "status": "sucesso",
        "dados": tarefas,
        "mensagem": "Tarefas listadas com sucesso"
    })


# OBTER UMA TAREFA
@app.route("/tarefas/<int:id>", methods=["GET"])
@jwt_required()
def obter(id):
    usuario_id = int(get_jwt_identity())
    tarefa = tarefa_service.obter_tarefa_por_id(id, usuario_id)

    if not tarefa:
        return jsonify({
            "status": "erro",
            "mensagem": "Tarefa não encontrada"
        }), 404

    return jsonify({
        "status": "sucesso",
        "dados": tarefa,
        "mensagem": "Tarefa encontrada"
    })


# CRIAR TAREFA
@app.route("/tarefas", methods=["POST"])
@jwt_required()
def criar():
    """
    ---
    tags:
      - Tarefas
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
           - titulo
          properties:
            titulo:
              type: string
              example: Estudar Flask
    response:
      201:
        description: Tarefa criada com sucesso
      400:
        description: Erro de validação
    """
    data = request.get_json()
    usuario_id = int(get_jwt_identity())

    try:
        tarefa = tarefa_service.criar_tarefa(data, usuario_id)
        return jsonify({
            "status": "sucesso",
            "dados": tarefa,
            "mensagem": "Tarefa criada com sucesso"
        }), 201
    except ValueError as erro:
        return jsonify({
            "status": "erro",
            "dados": None,
            "mensagem": str(erro)
        }), 400
# ATUALIZAR TAREFA
@app.route("/tarefas/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar(id):
    dados = request.get_json()

    if not dados:
        return jsonify({
            "status": "erro",
            "mensagem": "Dados inválidos"
        }), 400

    titulo = dados.get("titulo")
    concluida = dados.get("concluida")

    usuario_id = int(get_jwt_identity())
    tarefa = tarefa_service.atualizar_tarefa(id, titulo, concluida, usuario_id)

    if not tarefa:
        return jsonify({
            "status": "erro",
            "mensagem": "Tarefa não encontrada"
        }), 404

    return jsonify({
        "status": "sucesso",
        "dados": tarefa
    })


# DELETAR TAREFA
@app.route("/tarefas/<int:id>", methods=["DELETE"])
@jwt_required()
def deletar(id):

    usuario_id = int(get_jwt_identity())
    deletada = tarefa_service.deletar_tarefa(id, usuario_id)

    if not deletada:
        return jsonify({
            "status": "erro",
            "mensagem": "Tarefa não encontrada"
        }), 404

    return jsonify({
        "status": "sucesso",
        "dados": None,
        "mensagem": "Tarefa deletada com sucesso"
    })


# HEALTH CHECK
@app.route("/health")
def health():
    return jsonify({
        "status": "API funcionando"
    })


# REGISTRO DE USUÁRIO
@app.route("/registro", methods=["POST"])
def registrar_usuario():
    """
    ---
    tags:
      - Usuarios
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
            senha:
              type: string
    responses:
      200:
        description: Usuário registrado
    """

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "erro",
            "mensagem": "Dados não enviados"
        }), 400

    resultado = usuario_service.registrar_usuario(data)

    return jsonify(resultado)

# LOGIN DE USUARIO
@app.route("/login", methods=["POST"])
def login():
    """
    ---
    tags:
      - Usuarios
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            senha:
              type: string
    responses:
      200:
        description: Login realizado com sucesso
      401:
        description: Credenciais inválidas
    """

    data = request.get_json()

    email = data.get("email")
    senha = data.get("senha")

    usuario = usuario_service.autenticar(email, senha)

    if not usuario:
        return jsonify({
            "status": "erro",
            "mensagem": "Credenciais inválidas"
        }), 401

    token = create_access_token(identity=str(usuario["id"]))

    return jsonify({
        "status": "sucesso",
        "dados": {
            "token": token
        },
        "mensagem": "Login realizado com sucesso"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)
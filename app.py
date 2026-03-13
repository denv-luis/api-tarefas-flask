from flask import Flask, request, jsonify, render_template

from banco import criar_tabela
from services import tarefa_service
from services import usuario_service

app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    return render_template("index.html")


# LISTAR TAREFAS
@app.route("/tarefas", methods=["GET"])
def listar():
    tarefas = tarefa_service.listar_tarefas()

    return jsonify({
        "status": "sucesso",
        "dados": tarefas
    })


# OBTER UMA TAREFA
@app.route("/tarefas/<int:id>", methods=["GET"])
def obter(id):
    tarefa = tarefa_service.obter_tarefa_por_id(id)

    if not tarefa:
        return jsonify({
            "status": "erro",
            "mensagem": "Tarefa não encontrada"
        }), 404

    return jsonify({
        "status": "sucesso",
        "dados": tarefa
    })


# CRIAR TAREFA
@app.route("/tarefas", methods=["POST"])
def criar():
    data = request.get_json()

    try:
        tarefa = tarefa_service.criar_tarefa(data)
        return jsonify({
            "status": "sucesso",
            "dados": tarefa
        }), 201
    except ValueError as erro:
        return jsonify({
            "status": "erro",
            "mensagem": str(erro)
        }), 400
# ATUALIZAR TAREFA
@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()

    if not dados:
        return jsonify({
            "status": "erro",
            "mensagem": "Dados inválidos"
        }), 400

    titulo = dados.get("titulo")
    concluida = dados.get("concluida")

    if isinstance(titulo, dict):
        titulo = titulo.get("titulo")

    tarefa = tarefa_service.atualizar_tarefa(id, titulo, concluida)

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
def deletar(id):

    deletada = tarefa_service.deletar_tarefa(id)

    if not deletada:
        return jsonify({
            "status": "erro",
            "mensagem": "Tarefa não encontrada"
        }), 404

    return jsonify({
        "status": "sucesso",
        "mensagem": "Tarefa deletada"
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

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "erro",
            "mensagem": "Dados não enviados"
        }), 400

    resultado = usuario_service.registrar_usuario(data)

    return jsonify(resultado)


if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True, port=5001)
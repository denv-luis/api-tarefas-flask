from services import usuario_service
from banco import criar_tabela
from flask import Flask, request, jsonify
from services import tarefa_service
from flask import render_template

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("index.html")

@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(tarefa_service.listar_tarefas())

@app.route("/tarefas/<int:id>", methods=["GET"])
def obter(id):
    tarefa = tarefa_service.obter_tarefa_por_id(id)
    if tarefa:
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas", methods=["POST"])
def criar():
    data = request.get_json()

    if not data:
        return jsonify({"erro": "Dados não enviados"}), 400
    
    titulo = data.get("titulo")
    if not titulo or titulo.strip() == "":
        return jsonify({"erro": "O titulo da tarefa é obrigatório"}), 400

    tarefa = tarefa_service.criar_tarefa(data)
    return jsonify(tarefa), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    titulo = dados.get("titulo")
    concluida = dados.get("concluida")

    if isinstance(titulo, dict):
        titulo = titulo.get("titulo")
    tarefa = tarefa_service.atualizar_tarefa(id, titulo, concluida)

    if tarefa:
        return jsonify(tarefa)

    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar(id):
    if tarefa_service.deletar_tarefa(id):
        return jsonify({"mensagem": "Tarefa deletada"})

    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/health")
def health():
    return jsonify({"status": "API funcionando"})

@app.route("/registro", methods=["POST"])
def registrar_usuario():

    data = request.get_json()

    resultado = usuario_service.registrar_usuario(data)

    return jsonify(resultado)

if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True, port=5001)
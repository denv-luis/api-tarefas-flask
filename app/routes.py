from flask import Blueprint, jsonify

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify({"mensagem": "Lista de tarefas"})
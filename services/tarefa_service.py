from models.tarefa import Tarefa
from repositories import tarefa_repository
from datetime import datetime
import re

def listar_tarefas():
    tarefas = tarefa_repository.carregar()
    # converter sqlite Row para dict
    tarefas = [dict(t) for t in tarefas]

    # ordenar por data
    tarefas.sort(
        key=lambda t: t.get("data_criacao", ""),
        reverse=True
    )

    return tarefas

def obter_tarefa_por_id(id):
    tarefas = tarefa_repository.carregar()
    for t in tarefas:
        if t["id"] == id:
            return t
    return None

def criar_tarefa(data):

    print("DEBUG - criar_tarefa foi chamada")
    print("DEBUG - dados recebidos:", data)

    if not data:
        raise ValueError("Dados inválidos")
    titulo = data.get("titulo")
    if titulo is None:
        raise ValueError("O campo 'titulo' é obrigatório")
    if not isinstance(titulo, str):
        raise ValueError("O titulo deve ser texto")
    titulo = titulo.strip()
    if titulo == "":
        raise ValueError("O titulo não pode ser vazio")
    if not re.match(r"^[A-Za-zÀ-ÿ0-9 ]+$", titulo):
        raise ValueError("O titulo contém caracteres inválidos")
    
    data_criacao = datetime.now().strftime("%d %m %Y %H:%M")

    tarefa = Tarefa(
        id=None,
        titulo=titulo,
        data_criacao=data_criacao
    )

    tarefa_repository.criar(
        tarefa.titulo,
        tarefa.data_criacao
    )
    return tarefa.to_dict()

def atualizar_tarefa(id, titulo=None, concluida=None):
    tarefa_repository.atualizar(id, titulo, concluida)
    tarefas = tarefa_repository.carregar()

    for t in tarefas:
        if t["id"] == id:
            return dict(t)

    return None

def deletar_tarefa(id):
    tarefas = tarefa_repository.carregar()

    for t in tarefas:
        if t["id"] == id:
            tarefa_repository.deletar(id)
            return True

    return False
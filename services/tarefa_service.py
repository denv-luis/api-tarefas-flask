from models.tarefa import Tarefa
from repositories import tarefa_repository
from datetime import datetime

def listar_tarefas():
    return tarefa_repository.carregar()

def obter_tarefa_por_id(id):
    tarefas = tarefa_repository.carregar()
    for t in tarefas:
        if t["id"] == id:
            return t
    return None

def criar_tarefa(data):
    tarefas = tarefa_repository.carregar()
    novo_id = 1 if not tarefas else max(t["id"] for t in tarefas) + 1

    data_criacao = datetime.now().strftime("%d %m %Y %H:%M")

    tarefa = Tarefa(
        id=novo_id,
        titulo=str(data["titulo"]),
        data_criacao=data_criacao
    )

    tarefas.append(tarefa.to_dict())
    tarefa_repository.salvar(tarefas)
    return tarefa.to_dict()

def atualizar_tarefa(id, titulo=None, concluida=None):
    tarefas = tarefa_repository.carregar()

    for t in tarefas:
        if t["id"] == id:
            if titulo is not None:
                if isinstance(titulo, dict):
                    titulo = titulo.get("titulo", "")
                t["titulo"] = str(titulo)
            if concluida is not None:
                t["concluida"] = concluida
            tarefa_repository.salvar(tarefas)
            return t

    return None

def deletar_tarefa(id):
    tarefas = tarefa_repository.carregar()

    for t in tarefas:
        if t["id"] == id:
            tarefas.remove(t)
            tarefa_repository.salvar(tarefas)
            return True

    return False
from repositories import tarefa_repository
from schemas.tarefa_schema import TarefaSchema

schema = TarefaSchema()

def listar_tarefas(usuario_id):
    tarefas = tarefa_repository.listar(usuario_id)

    # ordenar por data
    tarefas.sort(
        key=lambda t: t.get("data_criacao") or "",
        reverse=True
    )

    return tarefas

def obter_tarefa_por_id(id, usuario_id):
    tarefas = tarefa_repository.listar(usuario_id)
    for t in tarefas:
        if t["id"] == id:
            return t
    return None

def criar_tarefa(data, usuario_id):
    if not data:
        raise ValueError("Dados inválidos")
    erros = schema.validate(data)
    if erros:
        raise ValueError(erros)
    titulo = data["titulo"].strip()

    return tarefa_repository.criar(titulo, usuario_id)

def atualizar_tarefa(id, titulo=None, concluida=None, usuario_id=None):
    tarefa = obter_tarefa_por_id(id, usuario_id)

    if not tarefa:
        return None
    tarefa_repository.atualizar(id, titulo, concluida)
    return obter_tarefa_por_id(id, usuario_id)

def deletar_tarefa(id, usuario_id):
    tarefa = obter_tarefa_por_id(id, usuario_id)

    if not tarefa:
            return False
    tarefa_repository.deletar(id)
    return True
from banco import conectar
from datetime import datetime

def carregar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    conn.close()

    return tarefas


def criar(titulo, usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (titulo, usuario_id) VALUES (?, ?)",
        (titulo, usuario_id)
    )

    conn.commit()
    tarefa_id = cursor.lastrowid

    cursor.execute(
        "SELECT id, titulo, concluida, data_criacao FROM tarefas WHERE id = ?",
        (tarefa_id,)
    )
    tarefa = cursor.fetchone()
    conn.close()

    return {
        "id": tarefa["id"],
        "titulo": tarefa["titulo"],
        "concluida": bool(tarefa["concluida"]),
        "data_criacao": tarefa["data_criacao"],
        "usuario_id": usuario_id
    }

def atualizar(id, titulo=None, concluida=None):
    conn = conectar()
    cursor = conn.cursor()

    if titulo is not None:
        cursor.execute(
            "UPDATE tarefas SET titulo=? WHERE id=?",
            (titulo, id)
        )

    if concluida is not None:
        cursor.execute(
            "UPDATE tarefas SET concluida=? WHERE id=?",
            (concluida, id)
        )

    conn.commit()
    conn.close()


def deletar(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

def listar(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, titulo, concluida, data_criacao FROM tarefas WHERE usuario_id = ?",
        (usuario_id,)
    )
    tarefas = cursor.fetchall()
    conn.close()
    tarefas_formatadas = [
        {
            "id": t[0],
            "titulo": t[1],
            "concluida": bool(t[2]),
            "data_criacao": t[3]
        }
        for t in tarefas
    ]
    return tarefas_formatadas
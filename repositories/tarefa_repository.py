from banco import conectar

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
        "INSERT INTO tarefas (titulo, data_criacao) VALUES (?, ?)",
        (titulo, usuario_id)
    )

    conn.commit()
    tarefa_id = cursor.lastrowid
    conn.close()

    return {
        "id": tarefa_id,
        "titulo": titulo,
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
    )
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas
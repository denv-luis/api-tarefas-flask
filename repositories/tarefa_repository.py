from banco import conectar

def carregar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    conn.close()

    return tarefas


def criar(titulo, data_criacao):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (titulo, data_criacao) VALUES (?, ?)",
        (titulo, data_criacao)
    )

    conn.commit()
    conn.close()


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
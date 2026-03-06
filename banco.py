import sqlite3

def conectar():
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        concluida BOOLEAN NOT NULL DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()
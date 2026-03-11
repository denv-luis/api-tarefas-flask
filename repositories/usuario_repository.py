from banco import conectar

def criar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nome, email, senha)
    VALUES (?, ?, ?)
    """, (nome, email, senha))

    conn.commit()
    conn.close()

def buscar_por_email(email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios WHERE email = ?
    """, (email,))

    usuario = cursor.fetchone()

    conn.close()
    return usuario
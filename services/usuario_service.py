from repositories import usuario_repository

def registrar_usuario(data):

    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")

    if not nome or not email or not senha:
        return {"erro": "Todos os campos são obrigatórios"}

    usuario_existente = usuario_repository.buscar_por_email(email)

    if usuario_existente:
        return {"erro": "Email já cadastrado"}

    usuario_repository.criar_usuario(nome, email, senha)

    return {"mensagem": "Usuário criado com sucesso"}
import bcrypt
from repositories import usuario_repository

def autenticar(email, senha):
    usuario = usuario_repository.buscar_por_email(email)
    if not usuario:
        return None
    if str(usuario["senha"]) != str(senha):
        return None
    return usuario
def registrar_usuario(data):

    nome = data.get("nome")
    email = data.get("email")
    senha = str(data.get("senha"))

    #validação
    if not nome or not email or not senha:
        return {"erro": "Todos os campos são obrigatórios"}

    usuario_existente = usuario_repository.buscar_por_email(email)

    if usuario_existente:
        return {"erro": "Email já cadastrado"}
    
    #criptografar senha
    senha_hash = bcrypt.hashpw(
        senha.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    #salvar no banco
    usuario_repository.criar_usuario(nome, email, senha_hash)

    return {"mensagem": "Usuário criado com sucesso"}
import bcrypt
from repositories import usuario_repository

def autenticar(email, senha):
    usuario = usuario_repository.buscar_por_email(email)
    if not usuario:
        return None
    senha_valida = bcrypt.checkpw(senha.encode(), usuario["senha"].encode())

    if not senha_valida:
        return None
    return usuario
def registrar_usuario(data):

    nome = data.get("nome")
    email = data.get("email")
    senha = str(data.get("senha"))

    #validação
    if not nome or not email or not senha:
        return {"status": "erro",
                "mensagem": "Todos os campos são obrigatórios"
                }
    #verificar se já existe
    usuario_existente = usuario_repository.buscar_por_email(email)

    if usuario_existente:
        return {"status": "erro",
                "dados": None,
                "mensagem": "Email já cadastrado"
                }
    
    #criptografar senha
    senha_hash = bcrypt.hashpw(
        senha.encode(),
        bcrypt.gensalt()
    )
    #montar usuario
    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha_hash
    }

    #salvar no banco
    return usuario_repository.salvar(usuario)
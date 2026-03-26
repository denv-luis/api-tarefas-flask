# 🚀 API de Tarefas com Flask

API REST desenvolvida com Flask para gerenciamento de tarefas, com autenticação de usuários utilizando JWT.

---

## 📌 Funcionalidades

- ✅ Cadastro de usuários
- 🔐 Login com autenticação JWT
- 📝 CRUD completo de tarefas:
  - Criar tarefa
  - Listar tarefas (por usuário)
  - Atualizar tarefa
  - Deletar tarefa
- 🔒 Proteção de rotas com JWT
- 📄 Documentação com Swagger

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- SQLite
- Flask-JWT-Extended
- Flasgger (Swagger)
- bcrypt

---

## 📂 Estrutura do projeto

api-tarefas-flask/
│
├── app.py
├── banco.py
├── models/
├── repositories/
├── services/
├── schemas/
├── templates/
├── static/
├── requirements.txt
└── README.md

---

## ⚙️ Como rodar o projeto

### 1. Clonar repositório

```bash
git clone https://github.com/denv-luis/api-tarefas-flask.git
cd api-tarefas-flask

2. Criar ambiente virtual

python -m venv venv
source venv/bin/activate

3. Instalar dependências

pip install -r requirements.txt

4. Rodar a aplicação

python app.py

A API estará disponível em:

http://127.0.0.1:5001

🔐 Autenticação
Login
POST /login

Retorna um token JWT.

Use esse token nas rotas protegidas:

Authorization: Bearer SEU_TOKEN

📌 Exemplos de uso

Criar tarefa

curl -X POST http://127.0.0.1:5001/tarefas \
-H "Authorization: Bearer SEU_TOKEN" \
-H "Content-Type: application/json" \
-d '{"titulo": "Minha tarefa"}'

Listar tarefas

curl http://127.0.0.1:5001/tarefas \
-H "Authorization: Bearer SEU_TOKEN"

📊 Status do projeto

🚧 Em desenvolvimento

👨‍💻 Autor

Luis

⭐ Melhorias futuras
Deploy em produção
Interface frontend
Paginação de tarefas
Filtros de busca
Testes automatizados
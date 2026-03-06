import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []

    with open(ARQUIVO_TAREFAS, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=4)
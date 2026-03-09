from datetime import datetime

class Tarefa:
    def __init__(self, id, titulo, concluida=False, data_criacao=None):
        self.id = id
        self.titulo = titulo
        self.concluida = concluida
        
        if data_criacao:
            self.data_criacao = data_criacao
        else:
            self.data_criacao = datetime.now().strftime("%d%m%Y %H:%M")

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "concluida": self.concluida,
            "data_criacao": self.data_criacao
        }
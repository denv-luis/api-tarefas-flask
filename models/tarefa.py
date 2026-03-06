class Tarefa:
    def __init__(self, id, titulo, concluida=False):
        self.id = id
        self.titulo = titulo
        self.concluida = concluida

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "concluida": self.concluida
        }
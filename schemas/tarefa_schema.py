from marshmallow import Schema, fields, validate

class TarefaSchema(Schema):
    titulo = fields.String(
        required=True,
        validate=validate.Length(min=1),
        error_messages={
            "required": "Título é obrigatório",
            "null": "Título não pode ser vazio"
        }
    )
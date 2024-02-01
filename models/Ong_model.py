import ormar
from db import BaseMeta

class Ong(ormar.Model):
    '''Definir o modelo de dados para Ong '''

    class Meta(BaseMeta):
        tablename = "ong"

    id_ong: int = ormar.Integer(primary_key=True, index=True)
    nome: str = ormar.String(max_length=100, nullable=False)
    cnpj: str = ormar.String(max_length=14, nullable=False)
    telefone: str = ormar.String(max_length=15, nullable=False)
    logradouro: str = ormar.String(max_length=100, nullable=False)
    cidade: str = ormar.String(max_length=50, nullable=False)
    estado: str = ormar.String(max_length=2, nullable=False)
    senha: str = ormar.String(max_length=100, nullable=False)
    cep: str = ormar.String(max_length=9, nullable=False)
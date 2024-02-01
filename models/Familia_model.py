import ormar
from db import BaseMeta

class Familia(ormar.Model):
    '''Definir o modelo de dados para Familia '''

    class Meta(BaseMeta):
        tablename = "familia"

    id_familia: int = ormar.Integer(primary_key=True, index=True)
    renda: float = ormar.Decimal(max_digits=10, decimal_places=2, nullable=False)
    numero_pessoas: int = ormar.Integer(nullable=False)
    cep: str = ormar.String(max_length=9, nullable=False)
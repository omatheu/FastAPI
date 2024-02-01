import ormar
from db import BaseMeta
from datetime import date
from ormar import ForeignKey, Model

from typing import Optional
from .Familia_model import Familia  # Import the Familia class from Familia.py

class Beneficiario(Model):
    class Meta(BaseMeta):
        tablename = "beneficiario"

    id_beneficiario: int = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    
    id_familia: Optional[Familia] = ForeignKey(Familia)
    
    nome: str = ormar.String(max_length=100, index=True, nullable=False)
    data_nascimento: date = ormar.Date(nullable=False)
    cpf: str = ormar.String(max_length=14, nullable=False)
    idade: int = ormar.Integer(nullable=False)
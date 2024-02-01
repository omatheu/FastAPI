from datetime import date
import ormar
from db import BaseMeta
from ormar import ForeignKey
from .Familia_model import Familia
from .CestaBasica_model import CestaBasica
from typing import Optional

class Coleta(ormar.Model):
    '''Definir o modelo de dados para Coleta '''

    class Meta(BaseMeta):
        tablename = "coleta"

    id_coleta: int = ormar.Integer(primary_key=True, index=True)
    data_coleta: date = ormar.Date(nullable=False)
    status: str = ormar.String(max_length=50, nullable=False)
    id_familia = ForeignKey(Familia)
    id_cesta_basica = ForeignKey(CestaBasica)
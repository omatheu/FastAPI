from datetime import date
import time
import ormar
from typing import Optional
from db import BaseMeta
from ormar import ForeignKey
from .Ong_model import Ong

class CestaBasica(ormar.Model):
    '''Definir o modelo de dados para Cesta Básica '''

    class Meta(BaseMeta):
        tablename = "cesta_basica"

    id_cesta_basica: int = ormar.Integer(primary_key=True, index=True)
    id_ong: Optional[Ong] = ForeignKey(Ong)
    data_entrega: date = ormar.Date(nullable=False)
    hora_entrega: time = ormar.Time(nullable=False)
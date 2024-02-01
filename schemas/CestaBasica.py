from pydantic import BaseModel, Field
from datetime import date, time
from pydantic.dataclasses import dataclass

# Definir o modelo Pydantic para o corpo da solicitação para CestaBasica
class CestaBasicaCreate(BaseModel):
    '''Schema para criar uma entidade cesta básica'''
    id_cesta_basica: int = Field(default=None, alias="id")
    id_ong: int = Field(default=None, alias="id_ong")
    data_entrega: date = Field(default=None, alias="data_entrega")
    hora_entrega: time = Field(default=None, alias="hora_entrega")

class CestaBasicaUpdate(BaseModel):
    '''Schema para alterar uma entidade cesta básica'''
    id_cesta_basica: int = Field(default=None, alias="id")
    id_ong: int = Field(default=None, alias="id_ong")
    data_entrega: date = Field(default=None, alias="data_entrega")
    hora_entrega: time = Field(default=None, alias="hora_entrega")
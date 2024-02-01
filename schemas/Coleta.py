from pydantic import BaseModel, Field
from datetime import date
from pydantic.dataclasses import dataclass

# Definir o modelo Pydantic para o corpo da solicitação para Coleta
class ColetaCreate(BaseModel):
    '''Schema para criar uma entidade Coleta'''
    id_familia: int = Field(default=None, alias="id_familia")
    id_coleta: int = Field(default=None, alias="id_coleta")
    id_cesta_basica: int = Field(default=None, alias="id_cesta_basica")
    data_coleta: date = Field(default=None, alias="data_coleta")
    status: str = Field(default=None, alias="status")

class ColetaUpdate(BaseModel):
    '''Schema para alterar uma entidade Coleta'''
    id_familia: int = Field(default=None, alias="id_familia")
    id_coleta: int = Field(default=None, alias="id_coleta")
    id_cesta_basica: int = Field(default=None, alias="id_cesta_basica")
    data_coleta: date = Field(default=None, alias="data_coleta")
    status: str = Field(default=None, alias="status")
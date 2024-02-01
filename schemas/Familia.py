from pydantic import BaseModel, Field
from decimal import Decimal
from pydantic.dataclasses import dataclass

# Definir o modelo Pydantic para o corpo da solicitação para Familia
class FamiliaCreate(BaseModel):
    '''Schema para criar uma entidade Família'''
    id_familia: int = Field(default=None, alias="id_familia")
    renda: Decimal = Field(default=None, alias="renda")
    numero_pessoas: int = Field(default=None, alias="numero_pessoas")
    cep: str = Field(default=None, alias="cep")

class FamiliaUpdate(BaseModel):
    '''Schema para alterar uma entidade Família'''
    renda: Decimal = Field(default=None, alias="renda")
    numero_pessoas: int = Field(default=None, alias="numero_pessoas")
    cep: str = Field(default=None, alias="cep")
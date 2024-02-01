from pydantic import BaseModel, Field
from datetime import date
from pydantic.dataclasses import dataclass

# Definir o modelo Pydantic para o corpo da solicitação para Beneficiario
class BeneficiarioCreate(BaseModel):
    '''Schema para a criar uma entidade Beneficiario'''
    id_familia: int = Field(default=None, alias="id_familia")
    id_beneficiario: int = Field(default=None, alias="id_beneficiario")
    nome: str = Field(default=None, alias="nome")
    data_nascimento: date = Field(default=None, alias="data_nascimento")
    cpf: str = Field(default=None, alias="cpf")
    idade: int = Field(default=None, alias="idade")

class BeneficiarioUpdate(BaseModel):
    '''Schema para a alterar uma entidade Beneficiario'''
    nome: str = Field(default=None, alias="nome")
    data_nascimento: date = Field(default=None, alias="data_nascimento")
    cpf: str = Field(default=None, alias="cpf")
    idade: int = Field(default=None, alias="idade")
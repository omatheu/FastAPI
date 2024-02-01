from pydantic import BaseModel, Field
from typing import List
from .CestaBasica import CestaBasicaCreate

# Definir o modelo de dados para Ong
# Define a classe Item

class OngSchema(BaseModel):
    id_ong : int = Field(default=None, alias="id_ong")
    nome : str = Field(default=None, alias="nome")
    cnpj : str = Field(default=None, alias="cnpj")
    telefone : str = Field(default=None, alias="telefone")
    logradouro : str = Field(default=None, alias="logradouro")
    cidade : str = Field(default=None, alias="cidade")
    estado : str = Field(default=None, alias="estado")
    senha : str = Field(default=None, alias="senha")
    cep : str = Field(default=None, alias="cep")
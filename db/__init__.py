import databases
import sqlalchemy
import ormar
from config import database_url

database = databases.Database(database_url)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata

from models.Ong_model import Ong
from models.Beneficiario_model import Beneficiario
from models.Familia_model import Familia
from models.Coleta_model import Coleta
from models.CestaBasica_model import CestaBasica

import db.db
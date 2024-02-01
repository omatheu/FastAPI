from db import metadata
import sqlalchemy
from config import database_url

engine = sqlalchemy.create_engine(database_url)

metadata.drop_all(engine)
metadata.create_all(engine)
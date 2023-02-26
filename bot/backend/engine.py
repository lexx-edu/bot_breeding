import sqlalchemy
from ..config import db_str

engine = sqlalchemy.create_engine(db_str)

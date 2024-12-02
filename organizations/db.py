from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from organizations.models import Base

MASTER_DB_URL = config("MASTER_DB_URL")

engine = create_engine(MASTER_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_master_db():
    Base.metadata.create_all(bind=engine)

def create_dynamic_db(db_url: str):
    dynamic_engine = create_engine(db_url)
    Base.metadata.create_all(bind=dynamic_engine)
    return dynamic_engine

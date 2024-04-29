from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

Base = declarative_base()
engine = create_engine(
    url = settings.DATABASE_URL_psycopg2
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

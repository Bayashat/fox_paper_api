from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

Base = declarative_base()

# SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost:5432/fox_paper"

engine = create_engine(
    url = settings.DATABASE_URL_psycopg2,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
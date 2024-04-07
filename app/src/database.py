from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import Settings

Base = declarative_base()

# SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost:5432/fox_paper"
settings = Settings()

engine = create_engine(
    url = settings.DATABASE_URL_psycopg2,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
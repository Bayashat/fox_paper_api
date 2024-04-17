from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:pa55word@db:5432/fox_paper")

engine = create_engine(
    DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(
    url = "postgresql://admin:admin@172.22.0.2:5432/fox_paper"
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

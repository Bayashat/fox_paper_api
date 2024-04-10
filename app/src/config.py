from pydantic_settings import BaseSettings, SettingsConfigDict

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

ALGORITHM = "HS256"

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://username:password@hostname:port/database
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    

    @property
    def DATABASE_URL_psycopg2(self):
        # postgresql+psycopg2://username:password@hostname:port/database
        # return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+psycopg2://admin:admin@localhost:5432/fox_paper"
    
    model_config = SettingsConfigDict(env_file=".env")
    
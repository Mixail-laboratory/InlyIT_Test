from pydantic import BaseSettings

class Settings(BaseSettings):
    database: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ad_service"

settings = Settings()
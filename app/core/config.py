from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Project"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./app.db"  # Значение по умолчанию

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    API_DOCS_BASE_URL: str = f"{API_V1_STR}/docs"
    PROJECT_NAME: str
    JWT_SECRET_KEY: str = secrets.token_urlsafe(255)
    JWT_TOKEN_EXPIRE_MINUTES: int
    JWT_TOKEN_GENERATION_ALGORITHM: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_MANAGEMENT_SYSTEM: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_URL: str
    OPEN_API_USER: str
    OPEN_API_USER_PASSWORD: str
    SQLALCHEMY_DATABASE_URI: str | None
    PORT: int = 5000
    PROD_MODE: bool

    class Config:
        env_file = ".env"

settings = Settings()


settings.SQLALCHEMY_DATABASE_URI = f"{settings.DATABASE_MANAGEMENT_SYSTEM}://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

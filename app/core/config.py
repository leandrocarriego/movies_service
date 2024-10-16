from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALLOW_CREDENTIALS: bool
    ALLOW_HEADERS: str
    ALLOW_METHODS: str
    ALLOW_ORIGINS: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

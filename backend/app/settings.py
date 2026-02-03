from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False


settings = Settings()
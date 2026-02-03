from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    DEBUG: bool = False
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int = 5432

    @property
    def database_url(self) -> str:
        return (f'postgresql+asyncpg://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}?'
                f'sslmode=require&channel_binding=require')


class Settings(BaseSettings):
    DEBUG: bool = False



settings = Settings()
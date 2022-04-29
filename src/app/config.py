import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_NAME: str

    APP_PORT: str

    SECRET_KEY: str = secrets.token_urlsafe(32)

    ALGORITHM: str = 'HS512'

    class Config:

        case_sensitive = True
        env_file = '.env'


settings = Settings()

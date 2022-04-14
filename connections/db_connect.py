from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from src.app.config import settings


def init_db_connection(app):
    app.db = create_engine(
        URL.create(
            "postgresql+psycopg2",
            username=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
        )
    )


def close_db_connection(app):
    try:
        app.db.dispose()
    except AttributeError:
        print('No DB was found!')

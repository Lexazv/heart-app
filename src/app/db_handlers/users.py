import sqlalchemy as sa
from passlib.context import CryptContext

from src.app.models import user

context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def create_user(conn, user_data):
    """ Create new user in db. """
    user_data.password = context.hash(user_data.password)

    return conn.execute(
        sa.insert(user).values(**user_data.dict()).returning('*')
    ).fetchone()


def get_user_by_email(conn, email):
    """ Get user from db by email """
    return conn.execute(
        sa.select(['*']).where(user.c.email == email)
    ).fetchone()


def check_user_by_email(conn, email):
    """ Check if user exists by email. """
    return conn.execute(
        sa.select([sa.exists().where(user.c.email == email)])
    ).fetchone()[0]

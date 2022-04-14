import os

import sqlalchemy as sa

from src.app.models import heart_data, file_data


def store_file_to_db(conn, file, user_id):
    """ Store file to db. """
    filename, extention = os.path.splitext(file.filename.split('/')[-1])

    return conn.execute(
        sa.insert(file_data)
        .values(filename=filename, extention=extention, user=user_id)
        .returning('*')
    ).fetchone()


def store_heart_data(conn, data, file):
    """ Store heart data to db. """
    for dataset in data:
        dataset.update(file=file)

    return conn.execute(
        sa.insert(heart_data).values(data)
    )


def get_files_by_user_id(conn, user_id):
    """ Get user files from db. """
    return conn.execute(
        sa.select(['*']).where(file_data.c.user == user_id)
    ).fetchall()


def delete_heart_data(conn, user_id):
    """ Delete heart data from db by user id. """
    return conn.execute(
        sa.delete(heart_data)
        .where(heart_data.c.user == user_id)
        .returning(heart_data.c.id, heart_data.c.user, heart_data.c.created_on)
    ).fetchone()
import os
from itertools import zip_longest
from concurrent.futures import ThreadPoolExecutor

import openpyxl
import requests

from src.services.auth import create_access_token


# Specify filename with users data here:
USERS_DATA_FILE = 'files/data.xlsx'

# Specify filename with heart data here:
# dict(<user_email>: <filename>) to store unique heart data from <filename> for each user with <user_email>.
HEART_DATA_STORAGE = {
    "testemaill@gmail.com": "files/request_file.csv",
    "temail@gamil.com": "files/request_file.csv"
}


def prepare_users_data(filename: str) -> list:
    file = openpyxl.load_workbook(filename=filename).active
    cols = ["email", "password", "first_name", "last_name", "confirmed_password"]

    users_data = [
        dict(
            zip_longest(
                cols, [cell.value for cell in row],
                fillvalue=file.cell(row=row_index + 2, column=2).value
            )
        ) for row_index, row in enumerate(file.iter_rows(min_row=2))
    ]

    return users_data


def fill_db_users(users_data: list) -> None:

    def _create_user(user_data: dict):
        response = requests.post(
            url='http://localhost:8000/api/users/registration', json=user_data
        )
        return response

    with ThreadPoolExecutor() as executor:
        responses = executor.map(_create_user, users_data)

    for response in responses:
        print(response.json())


def fill_db_heart_data(heart_data_storage: dict) -> None:
    heart_data_storage = list(HEART_DATA_STORAGE.items())

    def _create_heart_data(data_to_store: tuple):
        email, filename = data_to_store

        response = requests.post(
            url="http://localhost:8000/api/files/",
            json={"filename": os.path.abspath(filename)},
            headers={"Authorization": create_access_token(email=email)}
        )

        return response

    with ThreadPoolExecutor() as executor:
        responses = executor.map(_create_heart_data, heart_data_storage)

    for response in responses:
        print(response.json())


if __name__ == '__main__':
    users_data = prepare_users_data(filename=USERS_DATA_FILE)
    users_created = fill_db_users(users_data=users_data)

    if HEART_DATA_STORAGE:
        created_data = fill_db_heart_data(heart_data_storage=HEART_DATA_STORAGE)

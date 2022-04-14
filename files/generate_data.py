import os
from typing import List
from concurrent.futures import ThreadPoolExecutor

import requests
import openpyxl


# Specify filename with users data here:
users_data_file = './generate/data.xlsx'

# Specify filename with heart data here:
heart_data_file = ...


def prepare_users_data(filename: str) -> List[dict]:
    f = openpyxl.load_workbook(filename=filename).active

    cols = list(
        map(
            lambda c: c.value.lower().replace(' ', '_'), *f.iter_rows(max_row=1)
        )
    )
    users_data = [
        dict(
            zip(cols, [c.value for c in row])) for row in f.iter_rows(min_row=2)
    ]

    return users_data


def fill_db_users(users_data: dict) -> None:
    users_data['confirmed_password'] = users_data['password']

    response = requests.post(
        url='http://localhost:8000/api/users/registration', json=users_data
    )

    return response


if __name__ == '__main__':
    users_data = prepare_users_data(filename=users_data_file)

    with ThreadPoolExecutor() as executor:
        responses = executor.map(fill_db_users, users_data)

    for response in responses:
        print(response.json())

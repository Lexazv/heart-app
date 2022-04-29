from concurrent.futures import ThreadPoolExecutor
from typing import List

import openpyxl
import requests

# Specify filename with users data here:
users_data_file = 'files/data.xlsx'

# Specify filename with heart data here:
heart_data_file = ...


def prepare_users_data(filename: str) -> List[dict]:
    file = openpyxl.load_workbook(filename=filename).active

    cols = list(
        map(
            lambda column: column.value.lower()
            .replace(' ', '_'), *file.iter_rows(max_row=1)
        )
    )
    users_data = [
        dict(
            zip(
                cols, [c.value for c in row]
            )
        ) for row in file.iter_rows(min_row=2)
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

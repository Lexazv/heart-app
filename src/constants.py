from enum import Enum


class FileExtentions(Enum):

    csv = '.csv'


PASSWORD_TEMPLATE = '^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$'


EMAIL_TEMPLATE = '^[a-zA-Z0-9]{3,50}@[a-z]{2,10}.[a-z]{1,10}'


HEART_DATA_REQUIRED_COLUMNS = {
    'sex',
    'exng',
    'slp',
    'restecg',
    'thalachh',
    'cp',
    'age',
    'chol',
    'caa',
    'fbs',
    'trtbps',
    'thall',
    'oldpeak'
}


HEART_DATA_EQUAL_VALUE_COLS = ['age', 'sex']


class ErrorDetails(Enum):

    unaccaptable_columns = 'File contains unaccaptable columns.'
    invalid_personal_data = 'File contains invalid personal data.'
    invalid_age = 'Invalid age.'
    has_null_column = 'Columns in file contain nulls.'
    file_not_exist = 'Invalid filename.'

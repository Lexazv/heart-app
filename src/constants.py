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

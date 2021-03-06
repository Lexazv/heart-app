import numpy as np

from src.constants import ErrorDetails

HEART_DATA_VALID = [
    {
        "age": 63,
        "sex": 1,
        "cp": 3,
        "trtbps": 145,
        "chol": 233,
        "fbs": 1,
        "restecg": 0,
        "thalachh": 150,
        "exng": 0,
        "oldpeak": 2.3,
        "slp": 0,
        "caa": 0,
        "thall": 1,
    },
    {
        "age": 63,
        "sex": 1,
        "cp": 2,
        "trtbps": 130,
        "chol": 250,
        "fbs": 0,
        "restecg": 1,
        "thalachh": 187,
        "exng": 0,
        "oldpeak": 3.5,
        "slp": 0,
        "caa": 0,
        "thall": 2,
    },
    {
        "age": 63,
        "sex": 1,
        "cp": 1,
        "trtbps": 130,
        "chol": 204,
        "fbs": 0,
        "restecg": 0,
        "thalachh": 172,
        "exng": 0,
        "oldpeak": 1.4,
        "slp": 2,
        "caa": 0,
        "thall": 2,
    },
    {
        "age": 63,
        "sex": 1,
        "cp": 1,
        "trtbps": 120,
        "chol": 236,
        "fbs": 0,
        "restecg": 1,
        "thalachh": 178,
        "exng": 0,
        "oldpeak": 0.8,
        "slp": 2,
        "caa": 0,
        "thall": 2,
    },
    {
        "age": 63,
        "sex": 1,
        "cp": 0,
        "trtbps": 120,
        "chol": 354,
        "fbs": 0,
        "restecg": 1,
        "thalachh": 163,
        "exng": 1,
        "oldpeak": 0.6,
        "slp": 2,
        "caa": 0,
        "thall": 2,
    },
]


INVALID_HEART_DATA = [
    (
        [
            {
                "age": 63,
                "sex": 1,
                "cp": 3,
                "trtbps": 145,
                "chol": 233,
                "fbs": 1,
                "restecg": 0,
                "thalachh": 150,
                "exng": 0,
                "oldpeak": 2.3,
                "slp": 0,
                "caa": 0,
                "thall": 1,
                "invalid column": "value"
            }
        ],
        ErrorDetails.unaccaptable_columns.value
    ),
    (
        [
            {
                "age": np.nan,
                "sex": 1,
                "cp": 3,
                "trtbps": 145,
                "chol": 233,
                "fbs": 1,
                "restecg": 0,
                "thalachh": 150,
                "exng": 0,
                "oldpeak": 2.3,
                "slp": 0,
                "caa": 0,
                "thall": 1,
            },
        ],
        ErrorDetails.has_null_column.value
    ),
    (
        [
            {
                "age": 60,
                "sex": 0,
                "cp": 1,
                "trtbps": 120,
                "chol": 236,
                "fbs": 0,
                "restecg": 1,
                "thalachh": 178,
                "exng": 0,
                "oldpeak": 0.8,
                "slp": 2,
                "caa": 0,
                "thall": 2,
            },
            {
                "age": 63,
                "sex": 1,
                "cp": 0,
                "trtbps": 120,
                "chol": 354,
                "fbs": 0,
                "restecg": 1,
                "thalachh": 163,
                "exng": 1,
                "oldpeak": 0.6,
                "slp": 2,
                "caa": 0,
                "thall": 2,
            }
        ],
        ErrorDetails.invalid_personal_data.value
    ),
    (
        [
            {
                "age": 81,
                "sex": 0,
                "cp": 1,
                "trtbps": 120,
                "chol": 236,
                "fbs": 0,
                "restecg": 1,
                "thalachh": 178,
                "exng": 0,
                "oldpeak": 0.8,
                "slp": 2,
                "caa": 0,
                "thall": 2,
            }
        ],
        ErrorDetails.invalid_age.value
    )
]

# import pandas as pd
# from fastapi import HTTPException, status

from src.constants import HEART_DATA_REQUIRED_COLUMNS
from src.exceptions import HasNullColumnError, UnaccaptableColumnsError


def validate_df_columns(df):
    """ Check df has no unnecessary columns and others are named properly. """
    df_cols = set(df.columns)

    if not df_cols == HEART_DATA_REQUIRED_COLUMNS:
        diff_columns = list(
            df_cols.difference(HEART_DATA_REQUIRED_COLUMNS)
        )
        raise UnaccaptableColumnsError(columns=diff_columns)

    return True


def validate_df_null_values(df):
    """ Check df has no null values in required columns. """
    columns_with_null = list(df[df.columns[df.isnull().any()]])

    print(columns_with_null)

    if columns_with_null:
        raise HasNullColumnError(columns=columns_with_null)

    return True


def validate_heart_df(df):
    """ General df validation. """
    try:
        valid_columns = validate_df_columns(df=df)

        no_nulls = validate_df_null_values(df=df)

        equal_personal_data = all(
            map(lambda col: (df[col] == df[col][0]).all(), ['age', 'sex'])
        )

        valid_age = df['age'].min() >= 21 and df['age'].max() <= 80

    except KeyError:
        return False

    return (no_nulls and equal_personal_data and valid_age and valid_columns)


# def get_file_details(filename: str):
#     """ Validate dataframe and get dict with heart data. """
#     try:
#         df = pd.read_csv(filename) or None
#     except FileNotFoundError:
#         ...

#     if not validate_heart_df(df=df):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail='Invalid heart data. Please, check uploaded file!'
#         )
#     heart_data = df.to_dict('records')

#     return heart_data

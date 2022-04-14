import pandas as pd
from fastapi import HTTPException, status

from src.constants import HEART_DATA_REQUIRED_COLUMNS


def validate_df_columns(df):
    """ Check df has no unnecessary columns. """
    df_cols = set(df.columns)

    return df_cols == HEART_DATA_REQUIRED_COLUMNS


def valid_heart_df(df):
    """ General df validation. """
    try:
        valid_columns = validate_df_columns(df=df)

        no_nulls = not df.isnull().values.any()

        equal_personal_data = all(
            map(lambda col: (df[col] == df[col][0]).all(), ['age', 'sex'])
        )

        valid_age = df['age'].min() >= 21 and df['age'].max() <= 80

    except KeyError:
        return False

    return (no_nulls and equal_personal_data and valid_age and valid_columns)


def get_file_details(filename: str):
    """ Validate dataframe and get dict with heart data. """
    df = pd.read_csv(filename)

    if not valid_heart_df(df=df):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid heart data. Please, check uploaded file!'
        )
    heart_data = df.to_dict('records')

    return heart_data

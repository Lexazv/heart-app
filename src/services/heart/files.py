import pandas as pd

from src.exceptions import (
    HasNullColumnError,
    UnaccaptableColumnsError,
    InvalidPersonalData,
    InvalidAge,
    FileNotExist
)
from src.constants import (
    HEART_DATA_REQUIRED_COLUMNS, HEART_DATA_EQUAL_VALUE_COLS
)


def validate_df_columns(df: pd.DataFrame):
    """ Check df has no unnecessary columns and others are named properly. """
    df_cols = set(df.columns)

    if not df_cols == HEART_DATA_REQUIRED_COLUMNS:
        diff_columns = list(
            df_cols.difference(HEART_DATA_REQUIRED_COLUMNS)
        )
        raise UnaccaptableColumnsError(columns=diff_columns)

    return True


def validate_df_null_values(df: pd.DataFrame):
    """ Check df has no null values in required columns. """
    columns_with_null = list(df[df.columns[df.isnull().any()]])

    if columns_with_null:
        raise HasNullColumnError(columns=columns_with_null)

    return True


def validate_equal_personal_data(df: pd.DataFrame):
    """ Check personal data is equal. """
    not_equal_columns = list(
        filter(
            lambda col: (df[col] != df[col][0]).any(),
            HEART_DATA_EQUAL_VALUE_COLS
        )
    )
    if not_equal_columns:
        raise InvalidPersonalData(columns=not_equal_columns)
    
    return True


def validate_age(df: pd.DataFrame):
    """ Check user age is valid. """
    not_valid = df['age'][0] if df['age'][0] > 80 or df['age'][0] < 21 else None

    if not_valid:
        raise InvalidAge(value=not_valid)
    
    return True


def validate_heart_df(df: pd.DataFrame):
    """ General df validation. """
    validate_df_columns(df=df)
    validate_df_null_values(df=df)
    validate_equal_personal_data(df=df)
    validate_age(df=df)

    return True


def get_file_details(filename: str):
    """ Validate dataframe and get dict with heart data. """
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        raise FileNotExist(filename=filename)

    heart_data = df.to_dict('records')

    return heart_data

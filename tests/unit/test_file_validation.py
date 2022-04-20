import numpy as np
import pytest

from src.exceptions import HasNullColumnError, UnaccaptableColumnsError
from src.services.heart.files import (validate_df_columns,
                                      validate_df_null_values)
from tests.tests_data.files import EXCEPTIONS_INFO, REQUEST_FILE_DF


def test_validate_df_columns():
    result = validate_df_columns(df=REQUEST_FILE_DF)

    assert result


def test_validate_df_columns_exception(invalid_df):
    invalid_df['invalid_value'] = 12345

    with pytest.raises(UnaccaptableColumnsError) as exc:
        validate_df_columns(invalid_df)

    exception = exc._excinfo[1]

    assert exception.status_code == 400
    assert exception.detail == EXCEPTIONS_INFO[0]


def test_validate_df_null_values():
    result = validate_df_null_values(df=REQUEST_FILE_DF)

    assert result


def test_validate_df_null_values_exceptions(invalid_df):
    invalid_df['age'] = np.nan

    with pytest.raises(HasNullColumnError):
        validate_df_columns(invalid_df)

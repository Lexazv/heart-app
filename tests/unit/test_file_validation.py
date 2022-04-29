import pandas as pd
import pytest

from src.exceptions import (
    FileNotExist, 
    HasNullColumnError, 
    InvalidAge,
    InvalidPersonalData, 
    UnaccaptableColumnsError
)
from src.services.heart.files import (
    get_file_details, 
    validate_age,
    validate_df_columns,
    validate_df_null_values,
    validate_equal_personal_data)
from tests.tests_data.constants import MOCKED_FILES_PATH
from tests.tests_data.files import HEART_DATA_VALID, INVALID_HEART_DATA


def test_validate_df_columns():
    df = pd.DataFrame.from_records(data=HEART_DATA_VALID)
    result = validate_df_columns(df=df)

    assert result


@pytest.mark.parametrize("data, error", [INVALID_HEART_DATA[0]])
def test_validate_df_columns_exception(data, error):
    df = pd.DataFrame.from_records(data=data)

    with pytest.raises(UnaccaptableColumnsError) as exc:
        validate_df_columns(df)

    exception = exc._excinfo[1]

    assert exception.status_code == 400
    assert exception.detail == {
        'columns': ['invalid column'],
        'detail': error
    }


def test_validate_df_null_values():
    df = pd.DataFrame.from_records(data=HEART_DATA_VALID)
    result = validate_df_null_values(df=df)

    assert result


@pytest.mark.parametrize("data, error", [INVALID_HEART_DATA[1]])
def test_validate_df_null_values_exceptions(data, error):
    df = pd.DataFrame.from_records(data=data)

    with pytest.raises(HasNullColumnError) as exc:
        validate_df_null_values(df)

    exception = exc._excinfo[1]

    assert exception.status_code == 400
    assert exception.detail == {
        'columns': ['age'],
        'detail': error
    }


def test_validate_equal_personal_data():
    df = pd.DataFrame.from_records(data=HEART_DATA_VALID)
    result = validate_equal_personal_data(df=df)

    assert result


@pytest.mark.parametrize("data, error", [INVALID_HEART_DATA[2]])
def test_validate_equal_personal_data_exception(data, error):
    df = pd.DataFrame.from_records(data=data)

    with pytest.raises(InvalidPersonalData) as exc:
        validate_equal_personal_data(df)

    exception = exc._excinfo[1]

    assert exception.status_code == 400
    assert exception.detail == {
        'columns': ['age', 'sex'],
        'detail': error
    }


def test_validate_age():
    df = pd.DataFrame.from_records(data=HEART_DATA_VALID)
    result = validate_age(df=df)

    assert result


@pytest.mark.parametrize("data, error", [INVALID_HEART_DATA[3]])
def test_validate_age_exception(data, error):
    df = pd.DataFrame.from_records(data=data)

    with pytest.raises(InvalidAge) as exc:
        validate_age(df)

    exception = exc._excinfo[1]

    assert exception.status_code == 400
    assert exception.detail == {
        'value': 81,
        'detail': error
    }


def test_get_file_details():
    result = get_file_details(filename=f"{MOCKED_FILES_PATH}/request_file.csv")

    assert result == HEART_DATA_VALID


def test_get_file_details_exception():
    with pytest.raises(FileNotExist) as exc:
        get_file_details(filename="test_filename.csv")

    exception = exc._excinfo[1]

    assert exception.status_code == 400
    assert exception.detail == {
        "detail": "Invalid filename.", "filename": "test_filename.csv"
    }

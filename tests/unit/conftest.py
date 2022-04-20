from copy import copy
from unittest.mock import Mock

import pytest

from tests.tests_data.files import REQUEST_FILE_DF


@pytest.fixture
def mocked_obj():
    mock_obj = Mock()
    yield mock_obj


@pytest.fixture
def invalid_df():
    df = copy(REQUEST_FILE_DF)
    yield df

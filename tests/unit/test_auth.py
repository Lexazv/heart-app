import pytest
from jose.exceptions import JWTError

from src.services.auth import create_access_token, get_token_payload
from tests.tests_data.users import (PAYLOAD_DECODE_ARGS, PAYLOAD_ENCODE_ARGS,
                                    TOKEN_PAYLOAD, TOKEN_RESPONSE,
                                    USER_PROFILE)


@pytest.mark.parametrize(
    "email", [USER_PROFILE["email"], "email.com", "", "aaaaa", "email" * 100]
)
def test_create_token(email):
    result = create_access_token(email=email)

    assert result == TOKEN_RESPONSE
    assert isinstance(result["token"], str)


def test_get_token_encode_args(monkeypatch, mocked_obj):
    monkeypatch.setattr("src.services.auth.encode", mocked_obj)

    create_access_token(email=USER_PROFILE["email"])

    assert list(mocked_obj.call_args) == PAYLOAD_ENCODE_ARGS


@pytest.mark.parametrize(
    "email", [USER_PROFILE["email"], "email.com", "", "aaaaa", "email" * 100]
)
def test_get_token_payload(email):
    token = create_access_token(email=email)["token"]
    payload = get_token_payload(token)

    assert payload == TOKEN_PAYLOAD


@pytest.mark.parametrize(
    "token, exception",
    [
        ("", JWTError),
        ("asdasdasd", JWTError),
        (None, AttributeError),
        (123, AttributeError),
    ],
)
def test_get_token_payload_exception(token, exception):
    with pytest.raises(exception):
        get_token_payload(token)


def test_get_token_decode_args(monkeypatch, mocked_obj):
    monkeypatch.setattr("src.services.auth.decode", mocked_obj)

    token = create_access_token(email=USER_PROFILE["email"])["token"]
    get_token_payload(token)

    assert list(mocked_obj.call_args) == PAYLOAD_DECODE_ARGS

import pytest

from app.validators import validate_login
from tests.constants import (
    EMAIL_INVALID_ERROR,
    EMAIL_REQUIRED_ERROR,
    PASSWORD_INVALID_ERROR,
    PASSWORD_REQUIRED_ERROR,
    REMEMBER_ME_TYPE_ERROR,
)

@pytest.mark.parametrize(
    "password, expected_error",
    [
        ("", PASSWORD_REQUIRED_ERROR),
        ("123", PASSWORD_INVALID_ERROR)
    ]
)
def test_invalid_password(password, expected_error):
    result = validate_login("andrew@yandex.ru", password, True)

    assert result["is_valid"] is False
    assert result["errors"]["password"] == expected_error


@pytest.mark.parametrize(
    "remember_me, expected_error",
    [
        ("yes", REMEMBER_ME_TYPE_ERROR),
        (1, REMEMBER_ME_TYPE_ERROR),
        (None, REMEMBER_ME_TYPE_ERROR)
    ]
)
def test_invalid_type_remember_me(remember_me, expected_error):
    result = validate_login("andrew@yandex.ru", "12345678", remember_me)

    assert result["is_valid"] is False
    assert result["errors"]["remember_me"] == expected_error


@pytest.mark.parametrize(
    "password, expected_is_valid",
    [
        ("1234567", False),
        ("12345678", True),
        ("123456789", True)
    ]
)
def test_password_boundary_values(password, expected_is_valid):
    result = validate_login("andrew@yandex.ru", password, True)

    assert result["is_valid"] is expected_is_valid


@pytest.mark.parametrize(
    "remember_me",
    [
        True,
        False
    ]
)
def test_remember_me_accepts_boolean_values(remember_me):
    result = validate_login("andrew@yandex.ru", "12345678", remember_me)

    assert result["is_valid"] is True
    assert result["errors"] == {}
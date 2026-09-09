import pytest

from app.validators import validate_login
from tests.constants import (
    EMAIL_INVALID_ERROR,
    EMAIL_REQUIRED_ERROR,
    PASSWORD_INVALID_ERROR,
    PASSWORD_REQUIRED_ERROR,
    REMEMBER_ME_TYPE_ERROR,
)

@pytest.mark.smoke
def test_successful_login():
    result = validate_login("andrew@yandex.ru", "qwerty123", True)

    assert result["is_valid"] is True
    assert result["errors"] == {}


@pytest.mark.negative
def test_empty_email():
    result = validate_login("", "12345678", True)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == EMAIL_REQUIRED_ERROR


@pytest.mark.negative
def test_small_password():
    result = validate_login("andrew@yandex.ru", "123", True)

    assert result["is_valid"] is False
    assert result["errors"]["password"] == PASSWORD_INVALID_ERROR


@pytest.mark.negative
def test_email_without_dog():
    result = validate_login("andrewyandex.ru", "12345678", True)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == EMAIL_INVALID_ERROR


@pytest.mark.negative
def test_invalid_type():
    result = validate_login("andrew@yandex.ru", "12345678", "sada")

    assert result["is_valid"] is False
    assert result["errors"]["remember_me"] == REMEMBER_ME_TYPE_ERROR


@pytest.mark.negative
def test_login_with_multiple_invalid_fields():
    result = validate_login("", "123", "yes")

    assert result["is_valid"] is False
    assert result["errors"]["email"] == EMAIL_REQUIRED_ERROR
    assert result["errors"]["password"] == PASSWORD_INVALID_ERROR
    assert result["errors"]["remember_me"] == REMEMBER_ME_TYPE_ERROR


@pytest.mark.negative
def test_password_is_required():
    result = validate_login("andrew@yandex.ru", "", True)

    assert result["is_valid"] is False
    assert result["errors"]["password"] == PASSWORD_REQUIRED_ERROR


@pytest.mark.positive
def test_remember_me_can_be_false():
    result = validate_login("andrew@yandex.ru", "12345678", False)

    assert result["is_valid"] is True
    assert result["errors"] == {}
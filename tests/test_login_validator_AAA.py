import pytest
from app.validators import validate_login
from tests.constants import (
    EMAIL_INVALID_ERROR,
    EMAIL_REQUIRED_ERROR,
    PASSWORD_INVALID_ERROR,
    REMEMBER_ME_TYPE_ERROR,
)

@pytest.mark.negative
def test_email_without_dog():
    email = "andrewyandex.ru"
    password = "12345678"
    remember_me = True

    result = validate_login(email, password, remember_me)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == EMAIL_INVALID_ERROR


@pytest.mark.negative
def test_login_with_multiple_invalid_fields():
    email = ""
    password = "123"
    remember_me = "yes"

    result = validate_login(email, password, remember_me)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == EMAIL_REQUIRED_ERROR
    assert result["errors"]["password"] == PASSWORD_INVALID_ERROR
    assert result["errors"]["remember_me"] == REMEMBER_ME_TYPE_ERROR


@pytest.mark.negative
def test_email_is_required_but_remember_me_is_valid():
    email = ""
    password = "12345678"
    remember_me = False

    result = validate_login(email, password, remember_me)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == EMAIL_REQUIRED_ERROR
    assert "remember_me" not in result["errors"]
    assert "password" not in result["errors"]
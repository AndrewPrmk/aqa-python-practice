import pytest
from main import validate_login

@pytest.mark.negative
def test_email_without_dog():
    email = "andrewyandex.ru"
    password = "12345678"
    remember_me = True

    result = validate_login(email, password, remember_me)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is invalid"


@pytest.mark.negative
def test_login_with_multiple_invalid_fields():
    email = ""
    password = "123"
    remember_me = "yes"

    result = validate_login(email, password, remember_me)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is required"
    assert result["errors"]["password"] == "Password is invalid"
    assert result["errors"]["remember_me"] == "Remember me must be boolean"


@pytest.mark.negative
def test_email_is_required_but_remember_me_is_valid():
    email = ""
    password = "12345678"
    remember_me = False

    result = validate_login(email, password, remember_me)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is required"
    assert "remember_me" not in result["errors"]
    assert "password" not in result["errors"]
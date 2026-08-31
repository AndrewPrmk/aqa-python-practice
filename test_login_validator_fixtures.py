import pytest
from main import validate_login

@pytest.fixture
def valid_login_data():
    return {
        "email": "andrew@yandex.ru",
        "password": "12345678",
        "remember_me": True
    }

def test_successful_login(valid_login_data):
    result = validate_login(
        valid_login_data["email"],
        valid_login_data["password"],
        valid_login_data["remember_me"],
    )
    assert result["is_valid"] is True
    assert result["errors"] == {}


def test_email_is_required(valid_login_data):
    data = valid_login_data.copy()
    data["email"] = ""

    result = validate_login(
        data["email"],
        data["password"],
        data["remember_me"],
    )
    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is required"
    assert "password" not in result["errors"]
    assert "remember_me" not in result["errors"]


def test_password_is_required(valid_login_data):
    data = valid_login_data.copy()
    data["password"] = ""

    result = validate_login(
        data["email"],
        data["password"],
        data["remember_me"],
    )
    assert result["is_valid"] is False
    assert result["errors"]["password"] == "Password is required"
    assert "email" not in result["errors"]
    assert "remember_me" not in result["errors"]


@pytest.fixture
def valid_data_without_email(valid_login_data):
    data = valid_login_data.copy()
    data["email"] = ""
    return data


def test_login_data_without_email(valid_data_without_email):
    result = validate_login(
        valid_data_without_email["email"],
        valid_data_without_email["password"],
        valid_data_without_email["remember_me"]
    )
    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is required"
    assert "password" not in result["errors"]
    assert "remember_me" not in result["errors"]


@pytest.fixture
def login_data_with_short_password(valid_login_data):
    data = valid_login_data.copy()
    data["password"] = "123"
    return data

def test_login_data_with_short_password(login_data_with_short_password):
    result = validate_login(
        login_data_with_short_password["email"],
        login_data_with_short_password["password"],
        login_data_with_short_password["remember_me"],
    )
    assert result["is_valid"] is False
    assert result["errors"]["password"] == "Password is invalid"
    assert "email" not in result["errors"]
    assert "remember_me" not in result["errors"]
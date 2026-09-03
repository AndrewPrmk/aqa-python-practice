import pytest
from main import validate_login

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


def test_invalid_login_data(invalid_login_data):
    result = validate_login(
        invalid_login_data["email"],
        invalid_login_data["password"],
        invalid_login_data["remember_me"],
    )
    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is required"
    assert result["errors"]["password"] == "Password is invalid"
    assert result["errors"]["remember_me"] == "Remember me must be boolean"


def test_invalid_password_data(invalid_password_data, valid_login_data):
    data = valid_login_data.copy()
    data["password"] = invalid_password_data["password"]

    result = validate_login(
        data["email"],
        data["password"],
        data["remember_me"]
    )

    assert result["is_valid"] is False
    assert result["errors"]["password"] == invalid_password_data["expected_error"]


def test_invalid_email_data(invalid_email_data, valid_login_data):
    data = valid_login_data.copy()
    data["email"] = invalid_email_data["email"]

    result = validate_login(
        data["email"],
        data["password"],
        data["remember_me"]
    )

    assert result["is_valid"] is False
    assert result["errors"]["email"] == invalid_email_data["expected_error"]
    assert "password" not in result["errors"]
    assert "remember_me" not in result["errors"]


def test_invalid_remember_me_data(invalid_remember_me_data, valid_login_data):
    data = valid_login_data.copy()
    data["remember_me"] = invalid_remember_me_data["remember_me"]

    result = validate_login(
        data["email"],
        data["password"],
        data["remember_me"]
    )

    assert result["is_valid"] is False
    assert result["errors"]["remember_me"] == invalid_remember_me_data["expected_error"]
    assert "password" not in result["errors"]
    assert "email" not in result["errors"]
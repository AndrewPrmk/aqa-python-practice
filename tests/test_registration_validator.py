import pytest
from app.validators import validate_registration

def validate_registration_with_data(data):
    return validate_registration(
        data["email"],
        data["username"],
        data["password"],
        data["confirm_password"],
        data["accept_terms"],
)

@pytest.mark.parametrize(
    "username, expected_is_valid",
    [
        ("ab", False),
        ("abc", True),
        ("a" * 20, True),
        ("a" * 21, False),
    ]
)
def test_username_boundary_values(username, expected_is_valid, valid_registration_data):
    data = valid_registration_data.copy()
    data["username"] = username

    result = validate_registration(
        data["email"],
        data["username"],
        data["password"],
        data["confirm_password"],
        data["accept_terms"],
    )

    assert result["is_valid"] is expected_is_valid


@pytest.mark.parametrize(
    "password, expected_is_valid",
    [
        ("1234567", False),
        ("12345678", True),
        ("123456789", True),
    ]
)
def test_password_boundary_values(password, expected_is_valid, valid_registration_data):
    data = valid_registration_data.copy()
    data["password"] = password
    data["confirm_password"] = password

    result = validate_registration(
        data["email"],
        data["username"],
        data["password"],
        data["confirm_password"],
        data["accept_terms"],
    )

    assert result["is_valid"] is expected_is_valid


@pytest.mark.parametrize(
    "confirm_password, expected_error",
    [
        ("", "Confirm password is required"),
        ("different123", "Confirm password is invalid")
    ]
)
def test_confirm_password_validation(confirm_password, expected_error, valid_registration_data):
    data = valid_registration_data.copy()
    data["confirm_password"] = confirm_password

    result = validate_registration(
        data["email"],
        data["username"],
        data["password"],
        data["confirm_password"],
        data["accept_terms"]
    )

    assert result["is_valid"] is False
    assert result["errors"]["confirm_password"] == expected_error
    assert "email" not in result["errors"]
    assert "username" not in result["errors"]
    assert "password" not in result["errors"]
    assert "accept_terms" not in result["errors"]


@pytest.mark.parametrize(
    "accept_terms, expected_error",
    [
        (False, "Accept terms is invalid"),
        (None, "Accept terms is invalid"),
        ("yes", "Accept terms is invalid"),
    ]
)
def test_accept_terms_validation(accept_terms, expected_error, valid_registration_data):
    data = valid_registration_data.copy()
    data["accept_terms"] = accept_terms

    result = validate_registration(
        data["email"],
        data["username"],
        data["password"],
        data["confirm_password"],
        data["accept_terms"]
    )

    assert result["is_valid"] is False
    assert result["errors"]["accept_terms"] == expected_error
    assert "email" not in result["errors"]
    assert "username" not in result["errors"]
    assert "password" not in result["errors"]
    assert "confirm_password" not in result["errors"]


@pytest.mark.smoke
@pytest.mark.positive
def test_successful_registration(valid_registration_data):
    result = validate_registration_with_data(valid_registration_data)

    assert result["is_valid"] is True
    assert result["errors"] == {}

@pytest.mark.regression
@pytest.mark.negative
def test_registration_with_multiple_invalid_fields(valid_registration_data):
    data = valid_registration_data.copy()

    data["email"] = ""
    data["username"] = "ab"
    data["password"] = "123"
    data["confirm_password"] = ""
    data["accept_terms"] = False

    result = validate_registration(
        data["email"],
        data["username"],
        data["password"],
        data["confirm_password"],
        data["accept_terms"],
    )

    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is required"
    assert result["errors"]["username"] == "Username is invalid"
    assert result["errors"]["password"] == "Password is invalid"
    assert result["errors"]["confirm_password"] == "Confirm password is required"
    assert result["errors"]["accept_terms"] == "Accept terms is invalid"
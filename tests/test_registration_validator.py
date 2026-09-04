import pytest
from app.validators import validate_registration

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
    result = validate_registration(
        valid_registration_data["email"],
        valid_registration_data["username"],
        valid_registration_data["password"],
        valid_registration_data["confirm_password"],
        valid_registration_data["accept_terms"],
    )

    assert result["is_valid"] is True
    assert result["errors"] == {}




























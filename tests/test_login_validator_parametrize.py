import pytest
from main import validate_login

@pytest.mark.parametrize(
    "password, expected_error",
    [
        ("", "Password is required"),
        ("123", "Password is invalid")
    ]
)
def test_invalid_password(password, expected_error):
    result = validate_login("andrew@yandex.ru", password, True)

    assert result["is_valid"] is False
    assert result["errors"]["password"] == expected_error


@pytest.mark.parametrize(
    "remember_me, expected_error",
    [
        ("yes", "Remember me must be boolean"),
        (1, "Remember me must be boolean"),
        (None, "Remember me must be boolean")
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
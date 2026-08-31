from main import validate_login

def test_successful_login():
    result = validate_login("andrew@yandex.ru", "qwerty123", True)

    assert result["is_valid"] is True
    assert result["errors"] == {}


def test_empty_email():
    result = validate_login("", "12345678", True)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is required"


def test_small_password():
    result = validate_login("andrew@yandex.ru", "123", True)

    assert result["is_valid"] is False
    assert result["errors"]["password"] == "Password is invalid"


def test_email_without_dog():
    result = validate_login("andrewyandex.ru", "12345678", True)

    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is invalid"


def test_invalid_type():
    result = validate_login("andrew@yandex.ru", "12345678", "sada")

    assert result["is_valid"] is False
    assert result["errors"]["remember_me"] == "Remember me must be boolean"


def test_login_with_multiple_invalid_fields():
    result = validate_login("", "123", "yes")

    assert result["is_valid"] is False
    assert result["errors"]["email"] == "Email is required"
    assert result["errors"]["password"] == "Password is invalid"
    assert result["errors"]["remember_me"] == "Remember me must be boolean"


def test_password_is_required():
    result = validate_login("andrew@yandex.ru", "", True)

    assert result["is_valid"] is False
    assert result["errors"]["password"] == "Password is required"


def test_remember_me_can_be_false():
    result = validate_login("andrew@yandex.ru", "12345678", False)

    assert result["is_valid"] is True
    assert result["errors"] == {}
import pytest

@pytest.fixture
def valid_login_data():
    return {
        "email": "andrew@yandex.ru",
        "password": "12345678",
        "remember_me": True
    }

@pytest.fixture
def invalid_login_data():
    return {
        "email": "",
        "password": "123",
        "remember_me": "yes",
    }

@pytest.fixture(params=[
    {
        "password": "",
        "expected_error": "Password is required"
    },
    {
        "password": "123",
        "expected_error": "Password is invalid"
    },
])
def invalid_password_data(request):
    return request.param

@pytest.fixture(params=[
    {
        "email": "",
        "expected_error": "Email is required"
    },
    {
        "email": "andrewyandex.ru",
        "expected_error": "Email is invalid"
    },
])
def invalid_email_data(request):
    return request.param

@pytest.fixture(params=[
    {
        "remember_me": "yes",
        "expected_error": "Remember me must be boolean"
    },
    {
        "remember_me": 1,
        "expected_error": "Remember me must be boolean"
    },
    {
        "remember_me": None,
        "expected_error": "Remember me must be boolean"
    },
])
def invalid_remember_me_data(request):
    return request.param

@pytest.fixture
def valid_registration_data():
    return {
        "email": "andrew@yandex.ru",
        "username": "andrew",
        "password": "12345678",
        "confirm_password": "12345678",
        "accept_terms": True
    }
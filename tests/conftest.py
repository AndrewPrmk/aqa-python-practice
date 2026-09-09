import pytest

from tests.constants import (
    EMAIL_INVALID_ERROR,
    EMAIL_REQUIRED_ERROR,
    PASSWORD_INVALID_ERROR,
    PASSWORD_REQUIRED_ERROR,
    REMEMBER_ME_TYPE_ERROR,
)

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
        "expected_error": PASSWORD_REQUIRED_ERROR
    },
    {
        "password": "123",
        "expected_error": PASSWORD_INVALID_ERROR
    },
])
def invalid_password_data(request):
    return request.param

@pytest.fixture(params=[
    {
        "email": "",
        "expected_error": EMAIL_REQUIRED_ERROR
    },
    {
        "email": "andrewyandex.ru",
        "expected_error": EMAIL_INVALID_ERROR
    },
])
def invalid_email_data(request):
    return request.param

@pytest.fixture(params=[
    {
        "remember_me": "yes",
        "expected_error": REMEMBER_ME_TYPE_ERROR
    },
    {
        "remember_me": 1,
        "expected_error": REMEMBER_ME_TYPE_ERROR
    },
    {
        "remember_me": None,
        "expected_error": REMEMBER_ME_TYPE_ERROR
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
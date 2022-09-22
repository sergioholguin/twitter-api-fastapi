
# Libraries
import pytest
from fastapi import status
from .conftest import client, user_example


## Users

test_user_1 = {
    "username": user_example.email,
    "password": user_example.password
}

test_user_2 = {
    "username": "notindatabase@example.com",
    "password": user_example.password
}

test_user_3 = {
    "username": user_example.email,
    "password": "incorrectpassword"
}

test_users = [
    (test_user_1, status.HTTP_200_OK, ""),  # Successful Login
    (test_user_2, status.HTTP_401_UNAUTHORIZED, "Invalid Credentials"),  # User not in database
    (test_user_3, status.HTTP_401_UNAUTHORIZED, "Incorrect Password")  # Incorrect Password
]


# Testing Functions
@pytest.mark.auth
@pytest.mark.parametrize("user, expected_status, expected_details", test_users)
def test_user_logins(user, expected_status, expected_details):
    response = client.post("/login", data=user)
    assert response.status_code == expected_status
    if expected_details:
        assert response.json()["detail"] == expected_details

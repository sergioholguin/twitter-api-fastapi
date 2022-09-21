
# Libraries
import pytest
from fastapi import status
from .conftest import client


# Testing Functions

## Login Tests
@pytest.mark.auth
def test_user_login():
    user = {
        "username": "usertest1@example.com",
        "password": "thisisthetestpassword"
    }

    response = client.post("/login", data=user)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.auth
def test_user_not_in_db_login():
    user = {
        "username": "notindatabase@example.com",
        "password": "thisisthetestpassword"
    }

    response = client.post("/login", data=user)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Invalid Credentials"


@pytest.mark.auth
def test_user_incorrect_password_login():
    user = {
        "username": "usertest1@example.com",
        "password": "incorrectpassword"
    }

    response = client.post("/login", data=user)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Incorrect Password"


# @pytest.mark.user
# def test_show_user():
#     user_id = "0e99a9b9-20c7-43af-b968-c147a3ecf394"
#     response = client.get(f"/users/{user_id}")
#     assert response.status_code == 200
#     assert response.json() == {
#         "user_id": "0e99a9b9-20c7-43af-b968-c147a3ecf394",
#         "email": "anthony@example.com",
#         "first_name": "Anthony",
#         "last_name": "SomeLastName",
#         "country": "Peru",
#         "birth_date": "2001-01-01",
#         "creation_account_date": "2022-09-09"
#     }
#
#
# def test_show_nonexistent_user():
#     user_id = "00000000-0000-0000-0000-000000000000"
#     response = client.get(f"/users/{user_id}", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "User not found!"}


# def test_register_user():
#     response = client.post(
#         "/singup",
#         json={
#             "email": "test@example.com",
#             "password": "thisisthetestpassword",
#             "first_name": "Test",
#             "last_name": "SomeLastName",
#             "country": "Peru",
#             "birthday": "2001-01-01",
#             "creation_account_date": "2022-01-01"
#         }
#     )
#
#     assert response.status_code == 201
#     assert response.json() == {
#         "user_id": UUID,
#         "email": "test@example.com",
#         "password": "thisisthetestpassword",
#         "first_name": "Test",
#         "last_name": "SomeLastName",
#         "country": "Peru",
#         "birthday": "2001-01-01",
#         "creation_account_date": "2022-01-01"
#     }

# Libraries
import pytest
from fastapi import status
from fastapi.encoders import jsonable_encoder
from sql_app.hashing import get_password_hash, verify_password
from .conftest import user_example
from .conftest import client
from uuid import UUID


# Fixtures
@pytest.fixture
def hashed_password():
    return get_password_hash(password=user_example.password)


@pytest.mark.user
def test_register_user(hashed_password):
    db_user = {
        "user_id": UUID,
        "first_name": "Anthony",
        "last_name": "SomeLastName",
        "email": "anthony@example.com",
        "password": hashed_password,
        "country": "Peru",
        "birth_date": "2001-01-01",
        "creation_account_date": "2022-09-09"
    }

    response = client.post(
        "/signup",
        json={
            "first_name": "Anthony",
            "last_name": "SomeLastName",
            "email": "anthony@example.com",
            "password": user_example.password,
            "country": "Peru",
            "birth_date": "2001-01-01",
            "creation_account_date": "2022-09-09"
        }
    )

    response_info = response.json()

    # Remove Keys
    user_id = response_info.pop('user_id')
    db_user.pop('user_id')
    db_user_hashed_password = db_user.pop('password')

    assert response.status_code == status.HTTP_201_CREATED
    assert type(UUID(user_id)) == UUID
    assert verify_password(user_example.password, db_user_hashed_password) == True
    assert response_info == db_user


@pytest.mark.user
def test_register_email_already_registered(set_up_user):
    dummy_user, _ = set_up_user

    user_info = jsonable_encoder(dummy_user)
    response = client.post("/signup", json=user_info)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Email already registered"


# def test_show_nonexistent_user():
#     user_id = "00000000-0000-0000-0000-000000000000"
#     response = client.get(f"/users/{user_id}", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "User not found!"}





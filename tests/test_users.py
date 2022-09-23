
# Libraries
import pytest
from fastapi import status
from fastapi.encoders import jsonable_encoder
from sql_app.hashing import get_password_hash, verify_password
from .conftest import user_example
from .conftest import client
from uuid import UUID

# Models
from models import User


# Fixtures
@pytest.fixture
def hashed_password():
    return get_password_hash(password=user_example.password)


# Register Tests
@pytest.mark.create
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
    assert verify_password(user_example.password, db_user_hashed_password)
    assert response_info == db_user


@pytest.mark.create
@pytest.mark.user
def test_register_email_already_registered(set_up_users):
    dummy_user = set_up_users["user_1"]

    data_to_send = {
        "first_name": dummy_user.first_name,
        "last_name": dummy_user.last_name,
        "email": dummy_user.email,
        "password": user_example.password,
        "country": dummy_user.country,
        "birth_date": dummy_user.birth_date,
        "creation_account_date": dummy_user.creation_account_date
    }

    response = client.post("/signup", json=jsonable_encoder(data_to_send))

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Email already registered"


# Show users Tests
@pytest.mark.show
@pytest.mark.user
def test_show_all_users(set_up_users):
    dummy_header = set_up_users["header_1"]

    response = client.get('/users', headers=dummy_header)
    response_info = response.json()

    assert response.status_code == status.HTTP_200_OK

    # Verify if all response are tweets
    for user_dict_info in response_info:
        User(**user_dict_info)


@pytest.mark.show
@pytest.mark.user
@pytest.mark.parametrize("user, show_test", [("user_1", "show me"), ("user_2", "show user")])
def test_show_user(user, show_test, set_up_users):
    dummy_header = set_up_users["header_1"]
    user_to_search = set_up_users[user]

    user_id = user_to_search.user_id
    if user == "user_1":
        response = client.get(f"/users/me", headers=dummy_header)  # Testing show me
    else:
        response = client.get(f"/users/{user_id}", headers=dummy_header)  # Testing show user by ID

    expected_response = {
        "user_id": user_to_search.user_id,
        "email": user_to_search.email,
        "first_name": user_to_search.first_name,
        "last_name": user_to_search.last_name,
        "country": user_to_search.country,
        "birth_date": user_to_search.birth_date,
        "creation_account_date": user_to_search.creation_account_date
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == jsonable_encoder(expected_response)


@pytest.mark.show
@pytest.mark.user
def test_show_nonexistent_user(set_up_users):
    dummy_header = set_up_users["header_1"]

    user_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"/users/{user_id}", headers=dummy_header)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "User not found!"


# Delete users Tests
@pytest.mark.delete
@pytest.mark.user
def test_delete_user_failed(set_up_users):
    dummy_header = set_up_users["header_1"]

    user_id = "00000000-0000-0000-0000-000000000000"
    response = client.delete(f'/users/{user_id}/delete', headers=dummy_header)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "User doesn't exist!"


@pytest.mark.delete
@pytest.mark.user
def test_delete_user(set_up_users):
    dummy_header = set_up_users["header_1"]
    user_to_delete = set_up_users["user_2"]

    user_id = user_to_delete.user_id
    response = client.delete(f'/users/{user_id}/delete', headers=dummy_header)

    expected_response = {
        "user_id": user_id,
        "delete_message": f'{user_to_delete.first_name} has been deleted successfully!'
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


# Update users Tests
@pytest.mark.update
@pytest.mark.user
def test_update_user_failed(set_up_users):
    dummy_header = set_up_users["header_1"]
    user_to_update = set_up_users["user_2"]

    user_id = "00000000-0000-0000-0000-000000000000"

    data_to_send = {
        "first_name": "New First Name",
        "last_name": "New Last Name",
        "email": user_to_update.email,
        "password": user_example.password,
        "country": user_to_update.country,
        "birth_date": user_to_update.birth_date,
        "creation_account_date": user_to_update.creation_account_date
    }

    response = client.put(f'/users/{user_id}/update', json=jsonable_encoder(data_to_send), headers=dummy_header)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "User doesn't exist!"


@pytest.mark.update
@pytest.mark.user
def test_update_user(set_up_users):
    dummy_header = set_up_users["header_1"]
    user_to_update = set_up_users["user_2"]

    user_id = user_to_update.user_id

    data_to_send = {
        "first_name": "New First Name",
        "last_name": "New Last Name",
        "email": user_to_update.email,
        "password": user_example.password,
        "country": user_to_update.country,
        "birth_date": user_to_update.birth_date,
        "creation_account_date": user_to_update.creation_account_date
    }

    response = client.put(f'/users/{user_id}/update', json=jsonable_encoder(data_to_send), headers=dummy_header)

    expected_response = data_to_send.copy()
    expected_response.update({'user_id': user_id})
    expected_response.pop("password")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == jsonable_encoder(expected_response)




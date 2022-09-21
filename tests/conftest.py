# Testing
import pytest
from fastapi.testclient import TestClient

# Database
from models import UserRegister
from tests.test_sql_app import override_get_db
from sql_app.dependencies import get_db


# Others Tools
from sql_app import crud

# App
from main import app


password_example = "thisisthetestpassword"

app.dependency_overrides[get_db] = override_get_db


# Fixtures
@pytest.fixture(scope="session")
def client() -> TestClient:
    client = TestClient(app)
    yield client


@pytest.fixture(autouse=True)
def dummy_user(client):
    """Fixture to create test users before a test is run and delete them after it's completed."""

    # Define User
    test_user = UserRegister(
        first_name="UserTest1",
        last_name="SomeLastName",
        email="usertest1@example.com",
        password=password_example,
        country="Peru",
        birth_date="2001-01-01",
        creation_account_date="2022-01-01"
    )

    # Open DB Session
    test_database = next(override_get_db())

    # Add user to database
    db_user = crud.create_user_if_not_exist(test_database, test_user)

    # Login User
    response_user = client.post(
        "/singup",
        data={
            "email": db_user.email,
            "password": db_user.password,
        }
    )

    # Header
    print(response_user.json())
    header_user = {"Authorization": "Bearer " + response_user.json()["access_token"]}

    # Here is where the testing happens
    yield header_user

    # Delete user from database
    crud.delete_user(test_database, db_user.user_id)

# # Fixtures
# @pytest.fixture
# def hashed_password():
#     return get_password_hash(password=password_example)
#
#
# def set_up_users(hashed_password):
#     # First User
#     user_1 = {
#         "user_id": UUID,
#         "email": "usertest1@example.com",
#         "password": hashed_password,
#         "first_name": "UserTest1",
#         "last_name": "SomeLastName",
#         "country": "Peru",
#         "birthday": "2001-01-01",
#         "creation_account_date": "2022-01-01"
#     }
#
#     response_user_1 = client.post(
#         "/singup",
#         json={
#             "email": "usertest1@example.com",
#             "password": password_example,
#             "first_name": "UserTest1",
#             "last_name": "SomeLastName",
#             "country": "Peru",
#             "birthday": "2001-01-01",
#             "creation_account_date": "2022-01-01"
#         }
#     )
#
#     header_user_1 = {"Authorization": "Bearer " + response_user_1.json()["access_token"]}
#
#     # Second User
#     user_1_hashed_password = user_1.pop('password', None)
#
#     assert response_user_1.status_code == 201
#     assert verify_password(password_example, user_1_hashed_password) == True
#     assert response_user_1.json() == user_1

# Testing
import pytest
from fastapi.testclient import TestClient

# Database
from models import UserRegister
from tests.test_sql_app import override_get_db, mysql_test_engine
from sql_app.dependencies import get_db
from sql_app.database import Base

# Others Tools
from sql_app import crud

# App
from main import app


# Define User
user_example = UserRegister(
    first_name="UserTest1",
    last_name="SomeLastName",
    email="usertest1@example.com",
    password="thisisthetestpassword",
    country="Peru",
    birth_date="2001-01-01",
    creation_account_date="2022-01-01"
)


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


# Fixtures
@pytest.fixture
def set_db():
    Base.metadata.create_all(bind=mysql_test_engine)
    yield
    Base.metadata.drop_all(bind=mysql_test_engine)


@pytest.fixture(autouse=True)
def set_up_user(set_db):
    """Fixture to create test users before a test is run and delete them after it's completed."""

    # Define User
    test_user = user_example

    # Open DB Session
    test_database = next(override_get_db())

    # Add user to database
    db_user = crud.create_user_if_not_exist(test_database, test_user)

    # Login User
    response_user = client.post(
        "/login",
        data={
            "username": db_user.email,
            "password": user_example.password,
        }
    )

    # Header
    header_user = {"Authorization": "Bearer " + response_user.json()["access_token"]}

    # Here is where the testing happens
    yield test_user, header_user

    # Delete user from database
    crud.delete_user(test_database, db_user.user_id)

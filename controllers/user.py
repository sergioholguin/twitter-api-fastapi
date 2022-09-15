# Python
import json
from typing import List
from uuid import uuid4

# FastAPI
from fastapi import APIRouter, Depends
from fastapi import status, HTTPException
from fastapi import Path, Body

# Models
from models import User, UserRegister, UserDeleted

# Database
from sqlalchemy.orm import Session
from sql_app import crud, sqlalchemy_models as sql_models
from sql_app.database import mysql_engine as engine

# Dependencies
from .dependencies import get_db

# Tags
from .tags import Tags

# Examples
from examples import UserExamples

# Create database tables
sql_models.Base.metadata.create_all(engine)

router = APIRouter(tags=[Tags.users])


# Path Operation DatabaseTest
# @router.post("/data", response_model=List[User])
# def read_data(db: Session = Depends(get_db)):
#     users = crud.get_users(db)
#     print(users)
#     return users


# Users Path Operations

## Register a user
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a User'
)
def signup(user: UserRegister = Body(..., examples=UserExamples.user_info)):
    """
    SignUp

    This path operation register a user in the app

    Parameters:
    - Request Body parameters:
        - **user: UserRegister**

    Returns a json with the basic user information:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    - country: Optional[str]
    - birthday: Optional[PastDate]
    - creation_account_date: PastDate
    """
    with open('users.json', "r+", encoding="utf-8") as f:
        # Reading users.json and convert it to a dict
        content = f.read()
        results = json.loads(content)

        # Receive new user
        user_dict = user.dict()
        user_dict["user_id"] = str(uuid4())
        user_dict["birth_date"] = str(user_dict["birth_date"])
        user_dict["creation_account_date"] = str(user_dict["creation_account_date"])

        # Add new user to user.json
        results.append(user_dict)

        # Move to the first line of the file
        f.seek(0)

        # Writing the new user list
        json_user_list = json.dumps(results)
        f.write(json_user_list)
        f.truncate()

        return user_dict


## Login a user
@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a User'
)
def login():
    pass


## Show all users
@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users'
)
def show_all_users(db: Session = Depends(get_db)):
    """
    Show all users

    This path operation show all users in the app

    No-Parameters

    Returns a json list with all users in the app with the following keys:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    - country: Optional[str]
    - birthday: Optional[PastDate]
    - creation_account_date: PastDate
    """

    users = crud.get_users(db)
    return users


## Show a user
@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a specific user information'
)
def show_user(
        user_id: str = Path(
            ...,
            min_length=36,
            max_length=36,
            title="User ID",
            description="This is UUID4 that identifies a person.",
            examples=UserExamples.user_id
        ),
        db: Session = Depends(get_db)
):
    """
    Show User

    This path operation show a specific users given the ID

    Parameters:
    - Path Parameters:
        - **user_id: str**

    Returns a json with the user info with the following keys:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    - country: Optional[str]
    - birthday: Optional[PastDate]
    - creation_account_date: PastDate
    """

    user = crud.get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return user


## Delete a user
@router.delete(
    path="/users/{user_id}/delete",
    response_model=UserDeleted,
    status_code=status.HTTP_200_OK,
    summary='Delete a specific user account'
)
def delete_user(
        user_id: str = Path(
            ...,
            min_length=36,
            max_length=36,
            title="User ID",
            description="This is UUID4 that identifies a person.",
            examples=UserExamples.user_id
        )
):
    """
    Delete User

    This path operation remove a specific users given the ID

    Parameters:
    - Path Parameters:
        - **user_id: str**

    Returns a json with the user info with the following keys:
    - user_id: UUID
    - email: EmailStr
    - delete_message: str
    """

    with open("users.json", "r+", encoding="utf-8") as f:
        content = f.read()
        users = json.loads(content)

        try:
            # Searched user
            searched_user = [user for user in users if user["user_id"] == user_id][0]

            # Response
            response = {
                "user_id": searched_user["user_id"],
                "email": searched_user["email"],
                "delete_message": f'{searched_user["first_name"]} has been deleted!'
            }

            # Remove the specific user
            users.remove(searched_user)

            # Move to the first line of the file
            f.seek(0)

            # Writing the new user list
            json_user_list = json.dumps(users)
            f.write(json_user_list)
            f.truncate()

            return response

        except IndexError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This person doesn't exist!"
            )


## Update a user
@router.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a specific user account'
)
def update_user(
        user_id: str = Path(
            ...,
            min_length=36,
            max_length=36,
            title="User ID",
            description="This is UUID4 that identifies a person.",
            examples=UserExamples.user_id
        ),
        new_user_info: UserRegister = Body(..., examples=UserExamples.user_info)
):
    """
    Update User

    This path operation update user info in the app

    Parameters:
    - Path parameters:
        - **user_id: str**

    - Request Body parameters:
        - **new_user_info: UserRegister**

    Returns a json with the new user information:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    - country: Optional[str]
    - birthday: Optional[PastDate]
    - creation_account_date: PastDate
    """
    with open('users.json', "r+", encoding="utf-8") as f:
        # Reading users.json and convert it to a dict
        content = f.read()
        users = json.loads(content)

        # Searched user
        try:
            searched_user = [user for user in users if user["user_id"] == user_id][0]

            # New user info
            updated_user = new_user_info.dict()
            updated_user["user_id"] = searched_user["user_id"]
            updated_user["birth_date"] = str(updated_user["birth_date"])
            updated_user["creation_account_date"] = str(updated_user["creation_account_date"])

            # Replace user info
            index = users.index(searched_user)
            users[index] = updated_user

            # Move to the first line of the file
            f.seek(0)

            # Writing the new user list
            json_user_list = json.dumps(users)
            f.write(json_user_list)
            f.truncate()

            return updated_user

        except IndexError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This person doesn't exist!"
            )

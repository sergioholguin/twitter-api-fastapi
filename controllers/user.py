# Python
from typing import List

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
from sql_app.dependencies import get_db
from .oauth2 import get_current_user, auth_dependencies

# Tags
from .tags import Tags

# Examples
from examples import UserExamples

# Create database tables
sql_models.Base.metadata.create_all(engine)

router = APIRouter(tags=[Tags.users])


# Users Path Operations

## Register a user
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a User'
)
def signup(user: UserRegister = Body(..., examples=UserExamples.user_info), db: Session = Depends(get_db)):
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

    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    new_user = crud.create_user(db, user)
    return new_user


## Show all users
@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    dependencies=auth_dependencies
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

    db_users = crud.get_users(db)
    return db_users


## Show me
@router.get(
    path="/users/me",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show my information'
)
def show_user(
        current_user: User = Depends(get_current_user)
):
    """
    Show me

    This path operation show information about the login user

    No-Parameters

    Returns a json with the user info with the following keys:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    - country: Optional[str]
    - birthday: Optional[PastDate]
    - creation_account_date: PastDate
    """

    return current_user


## Show a user
@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a specific user information',
    dependencies=auth_dependencies
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

    db_user = crud.get_user_by_id(db, user_id)

    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return db_user


## Delete a user
@router.delete(
    path="/users/{user_id}/delete",
    response_model=UserDeleted,
    status_code=status.HTTP_200_OK,
    summary='Delete a specific user account',
    dependencies=auth_dependencies
)
def delete_user(
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

    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exist!")

    deleted_response = crud.delete_user(db, user_id)

    return deleted_response


## Update a user
@router.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a specific user account',
    dependencies=auth_dependencies
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
        new_user_info: UserRegister = Body(..., examples=UserExamples.user_info),
        db: Session = Depends(get_db)
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

    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exist!")

    updated_user = crud.update_user(db, user_id, new_user_info)

    return updated_user

# Python
import json
from typing import List
from uuid import UUID, uuid4

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Body

# Models
from models import User, UserRegister, UserLogin

# Tags
from .tags import Tags

# Examples
from examples import Examples


router = APIRouter(tags=[Tags.users])


# Users Path Operations

## Register a user
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a User'
)
def signup(user: UserRegister = Body(..., examples=Examples.singup)):
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
def show_all_users():
    """
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

    with open("users.json", "r", encoding="utf-8") as f:
        content = f.read()
        results = json.loads(content)

        return results


## Show a user
@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Show a specific user information'
)
def show_user():
    pass


## Delete a user
@router.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a specific user account'
)
def delete_user():
    pass


## Update a user
@router.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a specific user account'
)
def update_user():
    pass



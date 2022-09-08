# Python
import json
from typing import List
from enum import Enum

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

# Models
from models import User, UserRegister, UserBase, UserLogin
from models import Tweet, TweetBase

app = FastAPI()


# Tags
class Tags(Enum):
    users = 'users'
    tweets = 'tweets'


# Path Operations

## Users

### Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.users],
    summary='Register a User'
)
def signup(user: UserRegister = Body(...)):
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
    - creation_date: PastDate
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        # Reading users.json and convert it to a dict
        content = f.read()
        results = json.loads(content)

        # Receive new user
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        user_dict["creation_date"] = str(user_dict["creation_date"])

        # Add new user to user.json
        results.append(user_dict)

        # Move to the first line of the file
        f.seek(0)

        # Writing the new user list
        json_user_list = json.dumps(results)
        f.write(json_user_list)

        return user


### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Login a User'
)
def login():
    pass


### Show all users
@app.get(
    path="/users",
    ## response_model=List[User],
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
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
    - creation_date: PastDate
    """

    with open("users.json", "r", encoding="utf-8") as f:
        content = f.read()
        results = json.loads(content)

        return results


### Show a user
@app.get(
    path="/user/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Show a specific user information'
)
def show_user():
    pass


### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Delete a specific user account'
)
def delete_user():
    pass


### Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Update a specific user account'
)
def update_user():
    pass


## Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    tags=[Tags.tweets],
    summary="Show all tweets"
)
def home():
    return {"Twitter API": "Working!!"}


### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.tweets],
    summary='Post a tweet'
)
def post_tweet():
    pass


### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=[Tags.tweets],
    summary='Show a specific tweet'
)
def show_tweet():
    pass


### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=[Tags.tweets],
    summary='Delete a specific tweet'
)
def delete_tweet():
    pass


### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=[Tags.tweets],
    summary='Update a specific tweet'
)
def update_tweet():
    pass

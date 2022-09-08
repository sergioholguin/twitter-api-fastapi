# Python
from typing import List
from enum import Enum

# FastAPI
from fastapi import FastAPI
from fastapi import status

# Models
from models import User, UserBase, UserLogin
from models import TweetBase

app = FastAPI()


# Tags
class Tags(Enum):
    users = 'users'
    tweets = 'tweets'


# Path Operations

@app.get(path="/")
def home():
    return {"Twitter API": "Working!!"}


## Users
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.users],
    summary='Register a User'
)
def signup():
    pass


@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Login a User'
)
def login():
    pass


@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Show all users'
)
def show_all_users():
    pass


@app.get(
    path="/user/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Show a specific user information'
)
def show_user():
    pass


@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    summary='Delete a specific user account'
)
def delete_user():
    pass


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
@app.post(
    path="/post",
    response_model=TweetBase,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.tweets],
    summary='Create a tweet'
)
def create_tweet():
    pass


@app.get(
    path="/tweets/{tweet_id}",
    response_model=TweetBase,
    status_code=status.HTTP_200_OK,
    tags=[Tags.tweets],
    summary='Show a specific tweet'
)
def show_tweet():
    pass


@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=TweetBase,
    status_code=status.HTTP_200_OK,
    tags=[Tags.tweets],
    summary='Delete a specific tweet'
)
def delete_tweet():
    pass


@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=TweetBase,
    status_code=status.HTTP_200_OK,
    tags=[Tags.tweets],
    summary='Update a specific tweet'
)
def update_tweet():
    pass

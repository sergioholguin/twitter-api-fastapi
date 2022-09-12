# Python
import json
from typing import List
from enum import Enum
from uuid import UUID, uuid4

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

# Models
from models import User, UserRegister, UserLogin, Tweet

# Examples
from examples import Examples


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
    with open("users.json", "r+", encoding="utf-8") as f:
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
    - creation_account_date: PastDate
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
    """
    This path operation show all tweets in the app

    No-Parameters

    Returns a json list with all tweets in the app with the following keys:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """

    with open("tweets.json", "r", encoding="utf-8") as f:
        content = f.read()
        results = json.loads(content)

        return results


### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.tweets],
    summary='Post a tweet'
)
def post_tweet(tweet: Tweet = Body(...)):
    """
    Post Tweet

    This path operation post a tweet in the app

    Parameters:
    - Request Body parameters:
        - **tweet: Tweet**

    Returns a json with the basic tweet information:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        # Reading tweets.json and convert it to a dict
        content = f.read()
        results = json.loads(content)

        # Receive new tweet
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])

        if tweet_dict["updated_at"]:
            tweet_dict["updated_at"] = str(tweet_dict["updated_at"])

        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        tweet_dict["by"]["creation_account_date"] = str(tweet_dict["by"]["creation_account_date"])

        # Add new tweet to tweet.json
        results.append(tweet_dict)

        # Move to the first line of the file
        f.seek(0)

        # Writing the new tweet list
        json_tweet_list = json.dumps(results)
        f.write(json_tweet_list)

        return tweet


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

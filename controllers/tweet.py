# Python
import json
from typing import List
from uuid import UUID, uuid4

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Body

# Models
from models import Tweet

# Tags
from .tags import Tags

# Examples
from examples import Examples


router = APIRouter(tags=[Tags.tweets])


# Tweets Path Operations

## Show all tweets
@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
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


## Post a tweet
@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
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


## Show a tweet
@router.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a specific tweet'
)
def show_tweet():
    pass


## Delete a tweet
@router.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a specific tweet'
)
def delete_tweet():
    pass


## Update a tweet
@router.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a specific tweet'
)
def update_tweet():
    pass

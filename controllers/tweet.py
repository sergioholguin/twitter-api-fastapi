# Python
from datetime import datetime
from typing import List

# FastAPI
from fastapi import APIRouter, Depends
from fastapi import status, HTTPException
from fastapi import Path, Body

# Models
from models import Tweet, NewTweet, TweetDeleted, UpdateTweet

# Database
from sqlalchemy.orm import Session
from sql_app import crud, sqlalchemy_models as sql_models
from sql_app.database import mysql_engine as engine

# Dependencies
from .dependencies import get_db

# Tags
from .tags import Tags

# Examples
from examples import TweetExamples

# Create database tables
sql_models.Base.metadata.create_all(engine)

router = APIRouter(tags=[Tags.tweets])


# Tweets Path Operations

## Show all tweets
@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets"
)
def home(db: Session = Depends(get_db)):
    """
    Home

    This path operation show all tweets in the app

    No-Parameters

    Returns a json list with all tweets in the app with the following keys:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """

    db_tweets = crud.get_tweets(db)
    return db_tweets


## Post a tweet
@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a tweet'
)
def post_tweet(
        tweet: NewTweet = Body(..., examples=TweetExamples.tweet_info),
        db: Session = Depends(get_db)
):
    """
    Post Tweet

    This path operation post a tweet in the app

    Parameters:
    - Request Body parameters:
        - **tweet: NewTweet**

    Returns a json with the basic tweet information:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """

    db_tweet = crud.create_tweet(db, tweet)
    return db_tweet


## Show a tweet
@router.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a specific tweet'
)
def show_tweet(
        tweet_id: str = Path(
            ...,
            min_length=36,
            max_length=36,
            title="Tweet ID",
            description="This is UUID4 that identifies a tweet.",
            examples=TweetExamples.tweet_id
        ),
        db: Session = Depends(get_db)
):
    """
    Show Tweet

    This path operation show a specific tweet in the app

    Parameters:
    - Path Parameters:
        - **tweet_id: str**

    Returns a json list with the tweet info with the following keys:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """

    db_tweet = crud.get_tweet_by_id(db, tweet_id)

    if tweet_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tweet not found!")
    return db_tweet


## Delete a tweet
@router.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=TweetDeleted,
    status_code=status.HTTP_200_OK,
    summary='Delete a specific tweet'
)
def delete_tweet(
        tweet_id: str = Path(
            ...,
            min_length=36,
            max_length=36,
            title="Tweet ID",
            description="This is UUID4 that identifies a tweet.",
            examples=TweetExamples.tweet_id
        ),
        db: Session = Depends(get_db)
):
    """
    Delete Tweet

    This path operation delete a specific tweet in the app

    Parameters:
    - Path Parameters:
        - **tweet_id: str**

    Returns a json list with the tweet info with the following keys:
    - tweet_id: UUID
    - delete_message: str
    """

    db_tweet = crud.get_tweet_by_id(db, tweet_id=tweet_id)
    if db_tweet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tweet doesn't exist!")

    deleted_response = crud.delete_tweet(db, tweet_id)

    return deleted_response


## Update a tweet
@router.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a specific tweet'
)
def update_tweet(
        tweet_id: str = Path(
            ...,
            min_length=36,
            max_length=36,
            title="Tweet ID",
            description="This is UUID4 that identifies a tweet.",
            examples=TweetExamples.tweet_id
        ),
        new_tweet_info: UpdateTweet = Body(..., examples=TweetExamples.tweet_updates),
        db: Session = Depends(get_db)
):
    """
    Update Tweet

    This path operation update a specific tweet in the app

    Parameters:
    - Path Parameters:
        - **tweet_id: str**

    - Request Body parameters:
        - **new_tweet_info: UpdateTweet**

    Returns a json with the basic tweet information:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: datetime
    - by: User
    """

    db_tweet = crud.get_tweet_by_id(db, tweet_id=tweet_id)
    if db_tweet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tweet doesn't exist!")

    updated_tweet = crud.update_tweet(db, tweet_id, new_tweet_info)

    return updated_tweet

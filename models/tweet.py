# Python
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

# Pydantic
from pydantic import BaseModel, Field

# User
from models import User


class TweetBase(BaseModel):
    content: str = Field(..., min_length=0, max_length=280)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


class NewTweet(TweetBase):
    by: str = Field(..., min_length=36, max_length=36)


class TweetID(BaseModel):
    tweet_id: UUID = Field(default_factory=uuid4)


class Tweet(TweetBase, TweetID):
    by: User = Field(...)

    class Config:
        orm_mode = True


class TweetDeleted(TweetID):
    delete_message: str = Field(default="Tweet has been deleted!")


class UpdateTweet(TweetBase):
    pass

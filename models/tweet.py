# Python
from typing import Optional
from uuid import UUID, uuid4
from datetime import date

# Pydantic
from pydantic import BaseModel, Field


class TweetBase(BaseModel):
    content: str = Field(..., min_length=0, max_length=280)
    created_at: date = Field(default=date.today())
    updated_at: date = Field(default=date.today())


class NewTweet(TweetBase):
    user_id: Optional[UUID] = Field(default=None)


class TweetID(BaseModel):
    tweet_id: UUID = Field(default_factory=uuid4)


class Tweet(TweetBase, TweetID):
    user_id: UUID = Field(...)

    class Config:
        orm_mode = True


class TweetDeleted(TweetID):
    delete_message: str = Field(default="Tweet has been deleted!")


class UpdateTweet(TweetBase):
    pass

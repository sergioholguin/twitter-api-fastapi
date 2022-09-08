# Python
from typing import Optional
from uuid import UUID
from datetime import date, datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr, PastDate


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(..., min_length=8, max_length=64)


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    country: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[PastDate] = Field(default=None)
    age: int = Field(
        ...,
        gt=0,
        le=100
    )
    creation_date: PastDate


class TweetBase(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., min_length=0, max_length=280)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


class Tweet(TweetBase):
    pass
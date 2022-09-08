# Python
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr, PastDate


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(..., min_length=8)


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
    tweet_id: str = Field(..., min_length=10)
    tweet_content: str = Field(..., min_length=0, max_length=280)
    creation_date: PastDate
    last_update_date: PastDate


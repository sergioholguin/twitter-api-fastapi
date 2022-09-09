# Python
from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr, PastDate


class UserID(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)


class UserBase(BaseModel):
    email: EmailStr = Field(...)


class Password(BaseModel):
    password: str = Field(..., min_length=8, max_length=64)


class UserLogin(UserBase, Password):
    pass


class UserInfo(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
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
    creation_account_date: PastDate


class User(UserInfo, UserID):
    pass


class UserRegister(UserInfo, Password):
    pass


class TweetBase(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., min_length=0, max_length=280)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


class Tweet(TweetBase):
    pass

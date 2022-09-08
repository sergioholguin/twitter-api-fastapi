# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr, PastDate

# FastAPI
from fastapi import FastAPI

app = FastAPI()


# Models
class UserBase(BaseModel):
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
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=100
    )
    email: EmailStr
    creation_date: PastDate


class User(UserBase):
    password: str = Field(..., min_length=8)


class UserOut(UserBase):
    pass


class TweetBase(BaseModel):
    tweet_id: str = Field(..., min_length=10)
    tweet_content: str = Field(..., min_length=0, max_length=280)
    creation_date: PastDate
    last_update_date: PastDate


# Path Operations
@app.get(path="/")
def home():
    return {"Twitter API": "Working!!"}
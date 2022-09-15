# Python
from typing import Optional
from uuid import UUID, uuid4

# Pydantic
from pydantic import BaseModel, Field
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
    class Config:
        orm_mode = True


class UserRegister(UserInfo, Password):
    pass


class UserDeleted(UserID, UserBase):
    delete_message: str = Field(default="User has been deleted!")

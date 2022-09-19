
# Libraries
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from .token import verify_token, credentials_exception

from sql_app import crud
from sqlalchemy.orm import Session
from sql_app.dependencies import get_db


# Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_token(token)
    user = crud.get_user_by_email(db, email=token_data.email)

    if user is None:
        raise credentials_exception
    return user


# Auth Dependencies
auth_dependencies = [Depends(get_current_user)]

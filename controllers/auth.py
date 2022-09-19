# Python
from datetime import timedelta

# FastAPI
from fastapi import APIRouter, status, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

# Tags
from .tags import Tags

# Models
from models import UserLogin, Token

# Database
from sqlalchemy.orm import Session
from sql_app import crud, sqlalchemy_models as sql_models
from sql_app.database import mysql_engine as engine

# Dependencies
from sql_app.dependencies import get_db

# Hashing
from sql_app.hashing import verify_password

# Token
from .token import create_access_token
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Create database tables
sql_models.Base.metadata.create_all(engine)


router = APIRouter(tags=[Tags.auth])


# Auth Path Operations
@router.post(
    path="/login",
    response_model=Token,
    status_code=status.HTTP_200_OK,
    summary='Login a User'
)
def login(
        db: Session = Depends(get_db),
        ## request: UserLogin = Body(...)
        request: OAuth2PasswordRequestForm = Depends()
):
    db_user = crud.get_user_by_email(db, email=request.username)

    if db_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    if not verify_password(plain_password=request.password, hashed_password=db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")

    # Generate a JWT Token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}




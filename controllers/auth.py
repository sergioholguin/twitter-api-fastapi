
# FastAPI
from fastapi import APIRouter, status, Body, Depends, HTTPException

# Tags
from .tags import Tags

# Models
from models import UserLogin, User

# Database
from sqlalchemy.orm import Session
from sql_app import crud, sqlalchemy_models as sql_models
from sql_app.database import mysql_engine as engine

# Dependencies
from .dependencies import get_db

# Create database tables
sql_models.Base.metadata.create_all(engine)


router = APIRouter(tags=[Tags.auth])


# Auth Path Operations
@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a User'
)
def login(
        db: Session = Depends(get_db),
        request: UserLogin = Body(...)
):
    db_user = crud.get_user_by_email(db, email=request.email)

    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    # if
    return db_user



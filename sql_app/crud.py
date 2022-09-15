
from sqlalchemy.orm import Session

from .sqlalchemy_models import User, Tweet


# User Functions
## Read
def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


# Tweet Functions
## Read
def get_tweets(db: Session):
    return db.query(Tweet).all()



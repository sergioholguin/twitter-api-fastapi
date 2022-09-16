# UUID
from uuid import uuid4

# Session
from sqlalchemy.orm import Session

# SQLAlchemy Models
from .sqlalchemy_models import UserDB, TweetDB

# Pydantic Models
from models import UserRegister
from models import NewTweet, UpdateTweet

# Hashing
from .hashing import get_password_hash


# User Functions
## Read
def get_user_by_id(db: Session, user_id: str):
    return db.query(UserDB).filter(UserDB.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserDB).filter(UserDB.email == email).first()


def get_users(db: Session):
    return db.query(UserDB).all()


## Create
def create_user(db: Session, user: UserRegister):
    hashed_password = get_password_hash(user.password)

    db_user = UserDB(
        user_id=uuid4(),
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password,
        birth_date=user.birth_date,
        country=user.country,
        creation_account_date=user.creation_account_date
    )

    db.add(db_user)  # Add the new instance
    db.commit()  # Commit the changes to the database
    # Refresh the instance (so that it contains new data from the database, like the generated ID)
    db.refresh(db_user)

    return db_user


## Delete
def delete_user(db: Session, user_id: str):
    user_to_delete = get_user_by_id(db, user_id)
    db.query(UserDB).filter(UserDB.user_id == user_id).delete()
    db.commit()

    response = {
        "user_id": user_to_delete.user_id,
        "delete_message": f'{user_to_delete.first_name} has been deleted successfully!'
    }

    return response


## Update
def update_user(db: Session, user_id: str, new_user_info: UserRegister):
    # Updated Hashed Password
    hashed_password = get_password_hash(new_user_info.password)
    new_user_info.password = hashed_password

    # To Dict
    new_user_info = new_user_info.dict()

    # Updating Info
    db.query(UserDB).filter(UserDB.user_id == user_id).update(new_user_info)
    db.commit()

    return get_user_by_id(db, user_id=user_id)


# Tweet Functions
## Read
def get_tweets(db: Session):
    return db.query(TweetDB).all()


def get_tweet_by_id(db: Session, tweet_id: str):
    return db.query(TweetDB).filter(TweetDB.tweet_id == tweet_id).first()


## Create
def create_tweet(db: Session, tweet: NewTweet):
    db_tweet = TweetDB(
        tweet_id=uuid4(),
        content=tweet.content,
        created_at=tweet.created_at,
        updated_at=tweet.updated_at,
        user_id=tweet.user_id
    )

    db.add(db_tweet)  # Add the new instance
    db.commit()  # Commit the changes to the database
    # Refresh the instance (so that it contains new data from the database, like the generated ID)
    db.refresh(db_tweet)

    return db_tweet


## Delete
def delete_tweet(db: Session, tweet_id: str):
    tweet_to_delete = get_tweet_by_id(db, tweet_id)
    user = tweet_to_delete.user

    db.query(TweetDB).filter(TweetDB.tweet_id == tweet_id).delet()
    db.commit()

    response = {
        "tweet_id": tweet_to_delete.tweet_id,
        "delete_message": f'Tweet written by {user.first_name} has been deleted successfully!'
    }

    return response


## Update
def update_tweet(db: Session, tweet_id: str, new_tweet_info: UpdateTweet):
    new_tweet_info = new_tweet_info.dict()
    db.query(TweetDB).filter(TweetDB.tweet_id == tweet_id).update(new_tweet_info)
    db.commit()

    return get_tweet_by_id(db, tweet_id=tweet_id)


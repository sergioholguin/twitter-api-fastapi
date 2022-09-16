
# Libraries
from sqlalchemy import Column, ForeignKey, VARCHAR, DATE, TEXT
from sqlalchemy.orm import relationship

# Base from database.py
from .database import Base


# Classes
class UserDB(Base):
    __tablename__ = "users"

    # Attributes
    user_id = Column(VARCHAR(50), primary_key=True, index=True)
    first_name = Column(VARCHAR(20))
    last_name = Column(VARCHAR(20))
    email = Column(VARCHAR(20), unique=True, index=True)
    password = Column(VARCHAR(50))
    birth_date = Column(DATE)
    country = Column(VARCHAR(20), default=None)
    creation_account_date = Column(DATE)

    tweets = relationship("TweetDB", back_populates="user")


class TweetDB(Base):
    __tablename__ = "tweets"

    # Attributes
    tweet_id = Column(VARCHAR(50), primary_key=True, index=True)
    content = Column(TEXT)
    created_at = Column(DATE)
    updated_at = Column(DATE)
    user_id = Column(VARCHAR(50), ForeignKey("users.user_id"))

    user = relationship("UserDB", back_populates="tweets")

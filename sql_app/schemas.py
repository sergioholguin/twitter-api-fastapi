
from models import User, UserRegister, UserLogin, UserDeleted
from models import Tweet, NewTweet, TweetDeleted, UpdateTweet


class UserReading(User):
    class Config:
        orm_mode = True


class TweetReading(Tweet):
    class Config:
        orm_mode = True

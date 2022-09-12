# Python
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

# Pydantic
from pydantic import BaseModel, Field

# User
from models import User


class TweetBase(BaseModel):
    tweet_id: UUID = Field(default_factory=uuid4)
    content: str = Field(..., min_length=0, max_length=280)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


class Tweet(TweetBase):
    pass

# FastAPI
from fastapi import FastAPI

# Models
from models import User, UserBase, UserLogin
from models import TweetBase


app = FastAPI()


# Path Operations
@app.get(path="/")
def home():
    return {"Twitter API": "Working!!"}
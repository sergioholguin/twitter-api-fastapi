# Uvicorn
import uvicorn

# FastAPI
from fastapi import FastAPI

# Authentication
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Router
from controllers import router

app = FastAPI()

app.include_router(router)


@app.get("/test")
def auth_test(token: str = Depends(oauth_scheme)):
    return {"token": token}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

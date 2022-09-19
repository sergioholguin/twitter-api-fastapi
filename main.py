# Uvicorn
import uvicorn

# FastAPI
from fastapi import FastAPI

# Router
from controllers import router

app = FastAPI()

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

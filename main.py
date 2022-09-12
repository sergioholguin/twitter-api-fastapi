
# FastAPI
from fastapi import FastAPI

# Router
from controllers import router

app = FastAPI()

app.include_router(router)





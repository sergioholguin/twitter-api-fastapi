
# Starlette
from starlette.middleware.base import BaseHTTPMiddleware

# Uvicorn
import uvicorn

# FastAPI
from fastapi import FastAPI

# Router
from controllers import router

# Middleware
from middleware import process_time_header


# App
app = FastAPI()
app.include_router(router)
app.add_middleware(BaseHTTPMiddleware, dispatch=process_time_header)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

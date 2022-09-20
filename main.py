
# Starlette
from starlette.middleware.base import BaseHTTPMiddleware

# Uvicorn
import uvicorn

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Router
from controllers import router

# Middleware
from middleware import process_time_header

# CROS (Cros-Origin Resource Sharing)
from origins import cros_origins


# App
app = FastAPI()
app.include_router(router)

app.add_middleware(BaseHTTPMiddleware, dispatch=process_time_header)
app.add_middleware(
    CORSMiddleware,
    allow_origins=cros_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

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

# Metadata
from metadata import APIMetadata, tags_metadata


# App
app = FastAPI(
    title=APIMetadata["title"],
    description=APIMetadata["description"],
    version=APIMetadata["version"],
    terms_of_service=APIMetadata["terms_of_service"],
    contact=APIMetadata["contact"],
    license_info=APIMetadata["license_info"],
    openapi_tags=tags_metadata,
    docs_url="/docs",
    redoc_url=None
)

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

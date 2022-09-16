
# FastAPI
from fastapi import APIRouter

# Routers
from .user import router as user_router
from .tweet import router as tweet_router
from .auth import router as auth_router

router = APIRouter()

# Includes
router.include_router(user_router)
router.include_router(tweet_router)
router.include_router(auth_router)
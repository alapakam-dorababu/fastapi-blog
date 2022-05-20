from fastapi import APIRouter

from app.api import posts, users

api_routers = APIRouter()
api_routers.include_router(posts.router, tags=["Posts"])
api_routers.include_router(users.router, tags=["Authentication"])

from fastapi import APIRouter

from .short_link import router as short_link_router

routers = APIRouter()
routers.include_router(short_link_router)

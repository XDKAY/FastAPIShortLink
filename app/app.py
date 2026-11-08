from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.src.core.config.settings import settings
from app.src.db.database import database
from app.src.routers import routers


@asynccontextmanager
async def lifespan(_: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(
    title=settings.app.title,
    lifespan=lifespan,
)

app.include_router(routers)

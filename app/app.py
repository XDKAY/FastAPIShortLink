from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.src.db.database import connect, disconnect
from app.src.routers import routers


@asynccontextmanager
async def lifespan(_: FastAPI):
    await connect()
    yield
    await disconnect()


app = FastAPI(
    lifespan=lifespan
)

app.include_router(routers)

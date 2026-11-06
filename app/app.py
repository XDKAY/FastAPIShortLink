from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.src.db.database import connect, disconnect


@asynccontextmanager
async def lifespan(_: FastAPI):
    await connect()
    yield
    await disconnect()


app = FastAPI(
    lifespan=lifespan
)

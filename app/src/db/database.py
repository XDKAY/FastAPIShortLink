__all__ = ("connect", "disconnect", "get_session")

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from .base import Base
from app.src.core.config.settings import settings


EngineLocal = create_async_engine(settings.sqlite.url)
SessionLocal = async_sessionmaker(EngineLocal)


async def connect() -> None:
    async with EngineLocal.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def disconnect() -> None:
    await EngineLocal.dispose()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

__all__ = ("database", )

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from .base import Base
from app.src.core.config.settings import settings


class DatabaseHandler:
    def __init__(self, url: str) -> None:
        self._engine = create_async_engine(url)
        self._session = async_sessionmaker(self._engine)

    async def connect(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def disconnect(self) -> None:
        await self._engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session() as session:
            yield session


database = DatabaseHandler(settings.sqlite.url)

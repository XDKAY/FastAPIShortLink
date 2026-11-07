from uuid import UUID
from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from ..schemes.short_link import (
    ShortUrlResponseScheme,
    LongUrlInputScheme,
)
from app.src.db.model.short_link import ShortLinkModel


class AbstractSQLRepository(ABC):

    __model = None

    @abstractmethod
    async def add(self, long_url: LongUrlInputScheme, token: str) -> ShortUrlResponseScheme:
        ...

    @abstractmethod
    async def get_long_link(self, token: str) -> ShortUrlResponseScheme | None:
        ...

    @abstractmethod
    async def update_is_active(self, token: str) -> None:
        ...


class ShortLinkSQLRepository(AbstractSQLRepository):

    __model = ShortLinkModel

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, long_url: LongUrlInputScheme, token: str) -> ShortUrlResponseScheme:
        model = self.__model(
            token=token,
            long_url=str(long_url.url)
        )
        self._session.add(model)
        await self._session.commit()
        await self._session.refresh(model)
        return ShortUrlResponseScheme.model_validate(model)

    async def get_long_link(self, token: str) -> ShortUrlResponseScheme | None:
        stmt = select(self.__model).where(self.__model.token == token)
        model = (await self._session.execute(stmt)).scalar_one_or_none()
        if model:
            return ShortUrlResponseScheme.model_validate(model)

        return None

    async def update_is_active(self, token: str) -> None:
        stmt = update(self.__model).where(self.__model.token == token).values(is_active=True)
        await self._session.execute(stmt)
        await self._session.commit()

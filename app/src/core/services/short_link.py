from uuid import UUID
from ..repositories.short_link import AbstractSQLRepository
from ..schemes.short_link import (
    LongUrlInputScheme,
    ShortUrlResponseScheme
)
from ..utils.token import get_token


class ShortLinkService:
    def __init__(self, repo: AbstractSQLRepository) -> None:
        self._repo = repo

    async def add_link(self, long_url: LongUrlInputScheme) -> ShortUrlResponseScheme:
        token = await get_token()
        return await self._repo.add(long_url, token)

    async def get_long_url(self, token: str) -> ShortUrlResponseScheme | None:
        return await self._repo.get_long_link(token)

    async def update_is_active(self, token: str) -> None:
        await self._repo.update_is_active(token)

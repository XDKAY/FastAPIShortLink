from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.src.core.repositories.short_link import ShortLinkSQLRepository
from app.src.core.services.short_link import ShortLinkService
from app.src.db.database import get_session


SessionDep = Annotated[AsyncSession, Depends(get_session)]


async def get_short_link_service(session: SessionDep) -> ShortLinkService:
    return ShortLinkService(
        ShortLinkSQLRepository(session)
    )


ShortLinkServiceDep = Annotated[ShortLinkService, Depends(get_short_link_service)]

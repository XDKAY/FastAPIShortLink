from datetime import (
    datetime,
    timezone
)

from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException

from app.src.core.schemes.short_link import (
    LongUrlInputScheme,
    ShortUrlResponseScheme,
)
from app.src.core.utils.token import get_token_from_url
from app.src.dependencies.database import ShortLinkServiceDep



router = APIRouter(tags=["Short Link"])


@router.post("/api/short_link", status_code=status.HTTP_201_CREATED)
async def get_short_link(
    long_url: LongUrlInputScheme, short_link_service: ShortLinkServiceDep
) -> dict[str, str | ShortUrlResponseScheme]:
    short_link_scheme = await short_link_service.add_link(long_url)
    return {
        "url": f"http://localhost:8000/{short_link_scheme.token}",
        "data": short_link_scheme,
    }


@router.get("/{short_link}")
async def redirect(short_link: str, short_link_service: ShortLinkServiceDep):
    token = await get_token_from_url(short_link)

    if not token:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Url not found")

    model = await short_link_service.get_long_url(token)

    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Url not found"
            }
        )

    if model.is_active:
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail={
                "message": "Link has already been used"
            },
            headers={
                "Cache-Control": "no-cache"
            }
        )

    if datetime.now(timezone.utc).replace(tzinfo=None) >= model.exp_date:
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail={
                "message": "Exp date"
            }
        )

    await short_link_service.update_is_active(model.token)

    return RedirectResponse(model.long_url, status_code=status.HTTP_302_FOUND)

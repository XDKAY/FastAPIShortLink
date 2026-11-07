from uuid import UUID
from datetime import datetime

from pydantic import (
    BaseModel,
    AnyUrl,
    ConfigDict
)


class LongUrlInputScheme(BaseModel):
    url: AnyUrl


class ShortUrlResponseScheme(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID
    token: str
    long_url: str
    exp_date: datetime
    is_active: bool

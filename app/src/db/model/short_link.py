from uuid import UUID, uuid4
from datetime import datetime, timezone, timedelta

from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class ShortLinkModel(Base):
    __tablename__ = "ShortLinks"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    token: Mapped[str] = mapped_column(unique=True)
    long_url: Mapped[str]
    exp_date: Mapped[datetime] = mapped_column(
        default=lambda:
            datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(hours=1)
    )
    is_active: Mapped[bool] = mapped_column(default=False)

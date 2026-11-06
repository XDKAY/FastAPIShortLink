from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class ShortLinkModel(Base):
    __tablename__ = "ShortLinks"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    token: Mapped[str] = mapped_column(unique=True)
    long_url: Mapped[str]
    exp_date: Mapped[datetime]
    clicks: Mapped[bool] = mapped_column(default=False)

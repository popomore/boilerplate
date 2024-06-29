from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.dal.schema.base import Base


class UserSchema(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, nullable=False, primary_key=True, autoincrement=True
    )

    name: Mapped[str] = mapped_column(String, nullable=False)

    email: Mapped[str] = mapped_column(String, nullable=False)

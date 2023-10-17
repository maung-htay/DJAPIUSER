from db import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional


class ItemModel(db.Model):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    price: Mapped[float] = mapped_column(Integer, nullable=False)

    # one to many
    store_id: Mapped[int] = mapped_column(ForeignKey("stores.id"))
    store: Mapped["StoreModel"] = relationship(back_populates="items")

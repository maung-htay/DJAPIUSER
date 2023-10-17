from db import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)

    items: Mapped[List["ItemModel"]] = relationship(
        back_populates="store", lazy="dynamic")

from db import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship

class AuthorModel(db.Model):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    address_id = mapped_column(ForeignKey("address.id"))
    address = relationship("AddressModel", back_populates="author")
    books = relationship("BookModel", back_populates="author")
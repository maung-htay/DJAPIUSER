from db import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class AddressModel(db.Model):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(100),nullable=False)
    street: Mapped[str] = mapped_column(String(150),nullable=False)
    author = relationship("AuthorModel", uselist=False, back_populates="address")
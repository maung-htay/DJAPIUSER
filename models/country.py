from db import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class CountryModel(db.Model):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    books = relationship('BookModel', secondary='books_countrys', back_populates='countries')
    
    def __repr__(self):
        return f"<Country {self.name}>"
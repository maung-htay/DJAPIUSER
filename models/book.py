from db import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship

class BookCountry(db.Model):
    __tablename__ = 'books_countrys'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.id'))

class BookModel(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author = relationship("AuthorModel", back_populates="books") # , cascade="all, delete-orphan"
    countries = relationship('CountryModel', secondary='books_countrys', back_populates='books')
   
    

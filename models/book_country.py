from db import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship

class BookCountry(db.Model):
    __tablename__ = 'books_countrys'
    
    # id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'), primary_key=True)
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.id'), primary_key=True)
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

# jwt require
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import BookSchema,PlainBookSchema
from models import BookModel, AuthorModel, BookCountry, CountryModel

from db import db

blp = Blueprint("book", __name__, description="Operations on Country")

@blp.route("/book/")
class AuthorList(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return BookModel.query.all()
    
    
    @blp.arguments(BookSchema(partial=True))
    @blp.response(201, BookSchema)
    def post(self, book_data):
        print(book_data)
        # controlling for one to one relationship
        author = AuthorModel.query.get_or_404(book_data["author_id"])
        print(author)
        book = BookModel(name=book_data["name"],author_id=author.id)
        book_country = BookCountry(book_id=book.id,country_id=book_data["country_id"])
        try:
            db.session.add(book)
            db.session.commit()
            
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the books. {str(e)}")
            
        try:
            for id in list(book_data["country_id"]):
                country_id = CountryModel.query.get_or_404(id)
                book_country = BookCountry(book_id=book.id, country_id=country_id.id)
                db.session.add(book_country)

            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while inserting the books-country. {str(e)}")

            
             
        return book
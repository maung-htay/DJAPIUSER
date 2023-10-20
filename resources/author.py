from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

# jwt require
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import AuthorSchema, PlainAuthorSchema
from models import AuthorModel
from db import db

blp = Blueprint("authors", __name__, description="Operations on Author")

@blp.route("/author/")
class AuthorList(MethodView):
    @blp.response(200, AuthorSchema(many=True))
    def get(self):
        return AuthorModel.query.all()
    
    
    @blp.arguments(AuthorSchema)
    @blp.response(201, AuthorSchema)
    def post(self, author_data):
        # controlling for one to one relationship
        address = AuthorModel.query.filter(AuthorModel.address_id == author_data["address_id"]).first()
        if address is not None:
            abort(409, message="Address already exists.")
        author = AuthorModel(**author_data)
        try:
            db.session.add(author)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the address.")
        return author
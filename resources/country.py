from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

# jwt require
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import CountrySchema
from models import CountryModel
from db import db

blp = Blueprint("country", __name__, description="Operations on Country")

@blp.route("/country/")
class AuthorList(MethodView):
    @blp.response(200, CountrySchema(many=True))
    def get(self):
        return CountryModel.query.all()
    
    
    @blp.arguments(CountrySchema)
    @blp.response(201, CountrySchema)
    def post(self, country_data):
        # controlling for one to one relationship
        country = CountryModel(**country_data)
        try:
            db.session.add(country)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the address.")
        return country
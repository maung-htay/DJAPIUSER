from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

# jwt require
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import AddressSchema,PlainAddressSchema
from models import AddressModel
from db import db

blp = Blueprint("addresses", __name__, description="Operations on Address")

@blp.route("/address/")
class AddressList(MethodView):
    @blp.response(200, AddressSchema(many=True))
    def get(self):
        return AddressModel.query.all()
    
    @blp.arguments(PlainAddressSchema)
    @blp.response(201, AddressSchema)
    def post(self, address_data):
        address = AddressModel(**address_data)
        try:
            db.session.add(address)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the address.")
        return address
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import StoreSchema
from models import StoreModel
from db import db


blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/stores/")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()

        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the store.")

        return store

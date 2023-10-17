from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

# jwt require
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import ItemSchema, ItemUpdateSchema
from models import ItemModel
from db import db

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/items/")
class ItemsList(MethodView):
    @jwt_required()
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        current_identity = get_jwt_identity()
        print(current_identity)
        if current_identity.get("role") != "admin":
            abort(403, message="Admin privilege required.")
        return ItemModel.query.all()
    
    @jwt_required(fresh=True, optional=True)
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, store_data):
        item = ItemModel(**store_data)
        try:
            db.session.add(item)
            db.session.commit()

        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the store.")

        return item


@blp.route("/items/<int:item_id>")
class Item(MethodView):
    @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_id, item_data):
        item = ItemModel.query.get_or_404(item_id)
        item.price = item_data["price"]
        item.name = item_data["name"]
        db.session.add(item)
        db.session.commit()
        return item
    
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}
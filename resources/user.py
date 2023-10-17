from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, \
    get_jwt, get_jwt_identity


from schemas import UserSchema, LoginUserSchema
from models import UserModel
from db import db
from blocklist import BLOCKLIST


blp = Blueprint("users", __name__, description="Operations on user")

@blp.route("/register/")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(400, message="A user with that username already exists.")

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
            role=user_data["role"]
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201
    
@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200
    
@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(LoginUserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity={
                "username": user.username,
                "role": user.role,
                "id": user.id
                }, fresh=True)
            refresh_token = create_refresh_token(identity={
                "username": user.username,
                "role": user.role,
                "id": user.id
                })
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")    
        
@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        print(get_jwt())
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200    
    
@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"access_token": access_token}, 200  
        
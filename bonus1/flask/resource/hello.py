from flask.views import MethodView                # methodview: way of creating class based http method
from flask_smorest import Blueprint, abort
from schemas import HelloSchema
from sqlalchemy.exc import SQLAlchemyError

from models import HelloModel
from db import db

blp = Blueprint('hello', 'tags', description="")

@blp.route("/hello")
class FormHello(MethodView):
    @blp.response(200, HelloSchema(many=True))
    def get(self):
        return HelloModel.query.all()

    @blp.arguments(HelloSchema)
    @blp.response(201, HelloSchema)
    def post(self, data):
        user = HelloModel(**data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message="Something went wrong.")

        return user

@blp.route("/hello/<int:id>")
class User(MethodView):
    @blp.arguments(HelloSchema)
    @blp.response(200, HelloSchema)
    def put(self, user_data, id):
        user = HelloModel.query.get(id)
        if user:
            user.name = user_data['name']
            user.number = user_data["number"]
            user.email = user_data["email"]
        else:
            user = HelloModel(id=id, **user_data)
            db.session.add(user)
        db.session.commit()
        return user
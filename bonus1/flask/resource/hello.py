from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import HelloSchema

blp = Blueprint('hello', 'tags', description="")

@blp.route("/hello")
class FormHello(MethodView):
    @blp.arguments(HelloSchema)
    def post(self, data):
        return "hello" + " " + data['name']
        
    @blp.arguments(HelloSchema)
    @blp.response(201, HelloSchema)
    def put(self, data):
        print(data)
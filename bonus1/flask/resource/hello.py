from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint('hello', __name__, description="")

@blp.route("/hello")
class Hello(MethodView):
    def get(self):
        try:
            return {"message": 'Hello World'}
        except:
            abort(404, message="Routing Error")
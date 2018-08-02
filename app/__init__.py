from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)
from app.apis.controller.user_controller import api as auth_ns
from app.apis.controller.entries_controller import api as entries_ns

authorizatons = {
    "apikey":{
        "type": "apiKey",
        "in": "header",
        "name": "x-access-token"
    }
}

api = Api(
    blueprint,
    title='MyDiary',
    doc='/api/documentation',
    version='1.0',
    authorizations=authorizatons,
    description='MyDiary is an online journal where users can pen down their thoughts and feelings.'
)
del api.namespaces[0]
api.add_namespace(auth_ns, path="/api/v2/auth")
api.add_namespace(entries_ns, path="/api/v2")

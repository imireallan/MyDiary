from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)


api = Api(
    blueprint,
    title='MyDiary',
    doc='/api/documentation',
    version='1.0',
    description='MyDiary is an online journal where users can pen down their thoughts and feelings.'
)

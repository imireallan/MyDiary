from flask_restplus import Namespace, fields, reqparse

api = Namespace("auth", description="authentication related operations")

register_model = api.model('register_user', {
    'email': fields.String(required=True, description='email address'),
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password'),
    'confirm': fields.String(required=True, description='password')
})

login_model = api.model('login_user', {
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password')
})

register_parser = reqparse.RequestParser()

register_parser.add_argument('username', required=True, help='username should be a string')
register_parser.add_argument('email', required=True, help='email should be a string')
register_parser.add_argument('password', required=True, help='password should be a string')
register_parser.add_argument('confirm', required=True, help='password should be a string')

login_parser = register_parser.copy()
login_parser.remove_argument('email')
login_parser.remove_argument('confirm')
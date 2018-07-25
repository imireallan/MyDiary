# third-party imports
from flask_restplus import Resource
from flask_bcrypt import Bcrypt

# local imports
from ..models.model import User
from app.database import Database
from ..utils.user_model import api, register_parser, login_model, login_parser, register_model

# initializing our db connection
conn = Database()
cursor = conn.cursor
dict_cursor = conn.dict_cursor


@api.route("/signup")
class UserRegister(Resource):
    """Registers a new user."""

    @api.expect(register_model)
    def post(self):
        """handles registering a user """
        new_user = register_parser.parse_args()
        if new_user["password"] != new_user["confirm"]:
            return {"Warning": "Passwords do not match!!"}

        # check in the db if user exists
        user = User.get_user_by_username(dict_cursor, new_user["username"])
        if not user:
            hash_password = Bcrypt().generate_password_hash(new_user["password"]).decode()
            User.create_user(cursor, new_user["username"],new_user["email"],hash_password)
            return {"message": "User registered successfully"}
        return {"message": "User already exists. Please login."}, 400

@api.route("/login")
class LoginUser(Resource):
    "Class for logging in a user"

    @api.expect(login_model)
    def post(self):
        "Handles logging the user."
        args = login_parser.parse_args()
        if args["username"] and args["password"]:
            user = User.get_user_by_username(dict_cursor, args["username"])
            if user and Bcrypt().check_password_hash(user["password"], args["password"]):
                print(user)
                token = User.generate_token(user["id"])
                return {"message": "Logged in successfully", "token": token}
            return {"Warning": "No user found. Please sig up"},404
        return {"waning": "'username' and 'password' are required fields"}
                
                


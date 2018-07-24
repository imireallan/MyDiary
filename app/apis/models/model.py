from datetime import datetime, timedelta

import jwt
from flask import current_app
from flask_bcrypt import Bcrypt

class User():
    """Defines the User model"""
    def __init__(self, id, username, email, password,confirm):
        self.id = id
        self.username = username
        self.email = email
        self.password = Bcrypt().generate_password_hash(password)
        self.confirm = confirm

    def generate_token(self, user_id):
        """token generation for authentication"""
        try:
            payload = {"exp":datetime.utcnow() + timedelta(minutes=30),
                       "iat":datetime.utcnow(),
                       "sub":user_id}
            return jwt.encode(payload, current_app.config.get("SECRET_KEY")).decode()
        except Exception as e:
            return {"message": str(e)}

    @staticmethod
    def decode_token(token):
        """Decodes the access token"""

        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"))
            return payload['sub']

        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired. Please login"}
        
        except jwt.InvalidTokenError:
            return {"message":"Invalid token."}
    
    @staticmethod
    def create_user(cursor, username, email, password):
        query = "INSERT INTO users (username,email,password) VALUES ({},{},{})".format(username,email,password)
        cursor.execute(query)
    
    @staticmethod   
    def get_user_by_username(dict_cursor,username):
        query_string="SELECT * FROM users WHERE username = {}".format(username)
        dict_cursor.execute(query_string    )
        user = dict_cursor.fetchone()
        return user
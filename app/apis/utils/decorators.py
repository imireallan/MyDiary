from functools import wraps

from flask import request, current_app
import jwt
from ..models.model import User
from ..utils.entries_model import api
from app.database import Database

conn = Database()
dict_cursor = conn.dict_cursor

def token_required(f):
    """Ensures user is logged in before action
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        user_id = ""
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            
        if not token:
            api.abort(400, "Token Missing")
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"))
            user_id = payload['sub']

        except jwt.ExpiredSignatureError:
            api.abort(400, "Token has expired. Please login again")
        
        except jwt.InvalidTokenError:
            api.abort(400, "Invalid token")

        return f(user_id, *args, **kwargs)
    return wrap

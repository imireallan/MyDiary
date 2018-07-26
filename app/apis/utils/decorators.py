from functools import wraps

from flask import request, current_app
import jwt
from ..models.model import User
from app.database import Database

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
            return {"warning": "Token Missing"}
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"))
            user_id = str(payload['sub'])
            
        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired. Please login"}
        
        except jwt.InvalidTokenError:
            return {"warning":"Invalid token."}

        return f(user_id, *args, **kwargs)
    return wrap

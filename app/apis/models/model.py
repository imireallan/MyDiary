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
    
    @staticmethod
    def generate_token(user_id):
        """token generation for authentication"""
        try:
            payload = {"exp":datetime.utcnow() + timedelta(minutes=30),
                       "iat":datetime.utcnow(),
                       "sub":user_id}
            return jwt.encode(payload, current_app.config.get("SECRET_KEY")).decode()
        except Exception as e:
            return {"message": str(e)}
    
    @staticmethod
    def create_user(cursor, username, email, password):
        query = "INSERT INTO users (username,email,password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
    
    @staticmethod   
    def get_user_by_username(dict_cursor, username):
        query_string="SELECT * FROM users WHERE username = %s"
        dict_cursor.execute(query_string, [username])
        user = dict_cursor.fetchone()
        return user

class Entry(object):
    """Defines the User model"""
    def __init__(self, id, title, contents, user_id):
        self.id = id
        self.title = title
        self.contents = contents
        self.created_by = user_id
    
    @staticmethod
    def add_entry(cursor, title, contents, user_id):
        query = "INSERT INTO entries (title, contents, user_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, contents, user_id))
    
    @staticmethod   
    def get_entry_by_user_id(dict_cursor, user_id):
        query_string="SELECT * FROM entries WHERE use_id = %s"
        dict_cursor.execute(query_string, [user_id])
        entry = dict_cursor.fetchone()
        return entry

    @staticmethod   
    def get_entry_by_id(dict_cursor, id):
        query_string="SELECT * FROM entries WHERE id = %s"
        dict_cursor.execute(query_string, [id])
        entry = dict_cursor.fetchone()
        return entry

    @staticmethod   
    def modify_entry(cursor, title, contents, entryId, user_id):
        query = "UPDATE entries SET title=%s, contents=%s WHERE (Entryid=%s) AND (user_id=%s)"
        cursor.execute(query, (title, contents, entryId, user_id))

    @staticmethod   
    def delete_entry(cursor, entryId, user_id):
        query = "DELETE FROM entries WHERE (Entryid=%s) AND (user_id=%s)"
        cursor.execute(query, (entryId, user_id))

    @staticmethod   
    def get_all(dict_cursor, user_id):
        query_string="SELECT * FROM entries WHERE user_id = %s"
        dict_cursor.execute(query_string, [user_id])
        try:
            entries = dict_cursor.fetchall()
            results = []
            for entry in entries:
                obj = {
                    "id":entry["id"],
                    "title":entry["title"],
                    "contents":entry["contents"],
                    "user_id":entry["user_id"],
                    "created_at":entry["created_at"].strftime('%d-%b-%Y : %H:%M:%S'),
                }
                results.append(obj)
            return results
        except Exception as e:
            return {"message": str(e)}

        
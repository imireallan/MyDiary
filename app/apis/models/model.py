from datetime import datetime, timedelta

import jwt
from flask import current_app
from flask_bcrypt import Bcrypt

from ..utils.entries_model import api

class User():
    """Defines the User model"""
    def __init__(self, user_id, username, email, password, confirm):
        self.user_id = user_id
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
            return jwt.encode(payload, current_app.config.get("SECRET_KEY"))
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
    """Defines the Entry model"""
    def __init__(self, entry_id, title, contents, user_id):
        self.entry_id = entry_id
        self.title = title
        self.contents = contents
        self.created_by = user_id
    
    @staticmethod
    def add_entry(cursor, title, contents, user_id):
        query = "INSERT INTO entries (title, contents, user_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, contents, user_id))

    @staticmethod
    def get_entry_by_id(dict_cursor, entryId):
        query_string="SELECT * FROM entries WHERE id=%s"
        dict_cursor.execute(query_string, [entryId])
        data = dict_cursor.fetchone()
        if not data:
            api.abort(404, "Entry {} not found".format(entryId))
        entry = {key:str(value) for key, value in data.items() if value is not str}
        return entry
     

    @staticmethod   
    def modify_entry(dict_cursor, cursor, title, contents, entryId, user_id):
        data = Entry.get_entry_by_id(dict_cursor, entryId)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "UPDATE entries SET title=%s, contents=%s WHERE (id=%s)"
        cursor.execute(query, (title, contents, entryId))

    @staticmethod   
    def delete_entry(dict_cursor, cursor, entryId, user_id):
        data = Entry.get_entry_by_id(dict_cursor, entryId)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "DELETE FROM entries WHERE id=%s"
        dict_cursor.execute(query, [entryId])

    @staticmethod   
    def get_all(dict_cursor, user_id):
        query_string="SELECT * FROM entries WHERE user_id = %s"
        dict_cursor.execute(query_string, [user_id])
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

        
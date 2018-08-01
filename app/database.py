import os
# from manage import app

import psycopg2
import psycopg2.extras
import urllib.parse as urlparse


class Database(object):
    """Class for creating the database
    schema and establishing connection.
    """
    def __init__(self, testing=None):
        # with app.app_context():
        self.connection = self.connect(testing=testing)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def connect(self, testing=None):
        # db_uri = os.getenv("TEST_DB_URL") if testing else os.getenv("DATABASE_URL")
        db_uri = os.getenv("DATABASE_URL")
        result = urlparse.urlparse(db_uri)    
        host = result.hostname
        role = result.username
        pwd = result.password
        database = result.path[1:]

        return psycopg2.connect(
            db_host = "/tmp/.s.PGSQL.5432"
            db_port = False
            db_user = openerp
            db_password = False
        )

    # def connect_db(self):
    #     """Method for creating db connection."""
    #     try:
    #         self.connection = psycopg2.connect(database="diary_api", user="imire", password="pass@word1", host="localhost", port="5432")
    #         self.connection.autocommit = True
    #         self.cursor = self.connection.cursor()
    #         self.dict_cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #     except Exception as e:
    #         return {"message": str(e)}

    def create_tables(self):
        tables=(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS entries (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                title VARCHAR(255) NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                contents text,
                FOREIGN KEY (user_id)
                    REFERENCES users (id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
        )
        for table in tables:
            self.cursor.execute(table)
   
    def drop_all(self):
        tables=(
            """
            DROP TABLE IF EXISTS users CASCADE
            """,
            """
            DROP TABLE IF EXISTS entries CASCADE
            """
        )
        for table in tables:
            self.cursor.execute(table)
        

if __name__=="__main__":
    db = Database()
    db.create_tables()
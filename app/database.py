import os
# from manage import app

import psycopg2
import psycopg2.extras

# app = create_app(config_name=os.getenv("FLASK_CONFIG"))

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
        if testing:
            db_name = os.getenv("TEST_DB")       
        else:
            db_name = os.getenv("DATABASE")
        host = os.getenv("HOST")
        role = os.getenv("ROLE")
        pwd = os.getenv("PASSWORD")
        port = os.getenv("PORT")

        return psycopg2.connect(
            database=db_name,
            user=role,
            host=host,
            password=pwd,
            port=port
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
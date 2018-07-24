import psycopg2
import psycopg2.extras

class Database(object):
    """Class for creating the database
    schema and establishing connection.
    """
    def __init__(self):
        self.connect_db()
    
    def connect_db(self):
        """Method for creating db connection."""
        try:
            self.connection = psycopg2.connect(database="diary_api", user="imire", password="pass@word1", host="localhost", port="5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            self.dict_cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except Exception as e:
            return {"message": str(e)}

    def create_tables(self):
        tables=(
            """
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
            """,
            """
            CREATE TABLE entries (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                title VARCHAR(255) NOT NULL,
                creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                contents text,
                FOREIGN KEY (user_id)
                    REFERENCES users (id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
        )
        for table in tables:
            self.cursor.execute(table)
        

if __name__=="__main__":
    db = Database()
    db.create_tables()
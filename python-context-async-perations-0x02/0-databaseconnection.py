import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        print("Database connection opened.")
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.connection.commit()
            print("Transaction committed.")
        else:
            self.connection.rollback()
            print("Transaction rolled back due to error:", exc_val)

        self.connection.close()
        print("Database connection closed.")


with DatabaseConnection("test.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


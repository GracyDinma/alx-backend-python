import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.connection = None
        self.cursor = None

    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print("Database connection opened.")

        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.connection.commit()
            print("Transaction committed.")
        else:
            self.connection.rollback()
            print("Transaction rolled back due to error:", exc_val)

        self.connection.close()
        print("Database connection closed.")

with ExecuteQuery("test.db", "SELECT * FROM users WHERE age > ?", (25)) as results:
    for row in results:
        print(row)
import mysql.connector
from mysql.connector import Error

# Connecting to ALX_prodev database
def connect_to_prodev():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="ALX_prodev"
        )
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None
    

# Generator function to stream users one by one
def stream_users():
    conn = connect_to_prodev()
    if not conn:
        return
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    conn.close()


if __name__ == "__main__":
    for user in stream_users():
        print(user)
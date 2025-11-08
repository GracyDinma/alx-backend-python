import mysql
from mysql.connector import Error
import csv
import uuid

# Connecting to MySQL server

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'
        )
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists.")
    except Error as e:
        print(f"Error creating database: {e}")

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='ALX_prodev'
        )
        if connection.is_connected():
            print("Connected to ALX_prodev database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Create user_data table

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3,0) NOT NULL,
                INDEX (user_id)
           )
        """)
        connection.commit()
        print("Table user_data created or already exists.")
    except Error as e:
        print(f"Error creating table: {e}")


# Insert data from CSV if not exists

def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM user_data WHERE email = %s", (data['email']))
        exists = cursor.fetchone()[0]

        if not exists:
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (str(uuid.uuid4()), data['name'], data['email'], data['age']))
            connection.commit()
            print(f"Inserted: {data['name']}")
    except Error as e:
        print(f"Error inserting data: {e}")


# Generator to stream rows one by one

def stream_users(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    cursor.close()


# Main function to run setup

if __name__ == "__main__":
    server_conn = connect_db()
    if server_conn:
        create_database(server_conn)
        server_conn.close()

    db_conn = connect_to_prodev()
    if db_conn:
        create_table(db_conn)

        # Read CSV and insert data
        with open('user_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                insert_data(db_conn, row)

        # Stream rows one by one
        print("\nStreaming user rows:")
        for user in stream_users(db_conn):
            print(user)

        db_conn.close()




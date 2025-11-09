import mysql.connector
from mysql.connector import Error


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
    
# Yields user ages one by one

def stream_user_ages():
    conn = connect_to_prodev()
    if not conn:
        return

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield row['age']

    cursor.close()
    conn.close()

# Compute average age using generator

def compute_average_age():
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1

    if count == 0:
        return 0
    return total / count


if __name__ == "__main__":
    avg_age = compute_average_age()
    print(f"Average age of users: {avg_age:.2f}")
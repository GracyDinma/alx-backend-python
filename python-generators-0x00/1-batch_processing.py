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
    
# Fetching rows in batches
def stream_users_in_batches(batch_size):
    conn = connect_to_prodev()
    if not conn:
        return
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch

    cursor.close()
    conn.close()


# Process batches to filter users over age 25
def batch_processing(batch_size):
    for batch in stram_users_in_batches(batch_size):
        filtered = (user for user in batch if user['age'] > 25)
        yield list(filtered)

if __name__ == "__main__":
    BATCH_SIZE = 2

    for processed_batch in batch_processing(BATCH_SIZE):
        print("Processed batch:")
        for user in processed_batch:
            print(user)
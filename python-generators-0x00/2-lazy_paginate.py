import myaql.connector
from mysql.connector import Error

# Connect to ALX_prodev database

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
    
# Function to fetch a page of users from MySQL

def paginate_users(page_size, offset):
    conn = connect_to_prodev()
    if not conn:
        return []
    
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM user_data LIMIT %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows

# Lazily fetch pages

def lazy_paginate(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

if __name__ == "__main__":
    PAGE_SIZE = 2

    for page in lazy_paginate(PAGE_SIZE):
        print(f"Fetched page of {len(page)} users:")
        for user in page:
            print(user)

        print("----- End of page -----\n")
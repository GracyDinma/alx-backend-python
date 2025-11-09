import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect("test.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("All users:", users)
            return users
        

async def async_fetch_older_users():
    async with aiosqlite.connect("test.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > ?" (40,)) as cursor:
             older_users = await cursor.fetchall()
             print("Users older than 40:", older_users)
             return older_users
        
async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("\nConcurrent Results:", results)


    if __name__ == "__main__":
        asyncio.run(fetch_concurrently())
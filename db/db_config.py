from psycopg import AsyncConnection, connect
import psycopg
import asyncio

db_data = "dbname=db_auth user=admin password=root"


async def connection():
    async with await AsyncConnection.connect(db_data) as aconn:
        async with aconn.cursor() as cur:
            return await cur


if __name__ == "__main__":
    asyncio.run(connection())

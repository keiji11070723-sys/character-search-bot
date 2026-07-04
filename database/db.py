import asyncpg
from config import DATABASE_URL


class Database:

    def __init__(self):
        self.pool = None

    async def connect(self):
        """PostgreSQLへ接続"""
        self.pool = await asyncpg.create_pool(DATABASE_URL)

    async def create_tables(self):
        """初回起動時にテーブルを作成"""

        async with self.pool.acquire() as conn:

            await conn.execute("""
                CREATE TABLE IF NOT EXISTS characters (

                    id SERIAL PRIMARY KEY,

                    name TEXT UNIQUE NOT NULL,

                    attribute TEXT NOT NULL,

                    rarity TEXT NOT NULL

                );
            """)

    async def add_character(self, name, attribute, rarity):

        async with self.pool.acquire() as conn:

            await conn.execute("""
                INSERT INTO characters(name, attribute, rarity)

                VALUES($1,$2,$3)

                ON CONFLICT(name)
                DO NOTHING;
            """, name, attribute, rarity)

    async def search_character(self, keyword):

        async with self.pool.acquire() as conn:

            return await conn.fetch("""
                SELECT *

                FROM characters

                WHERE name ILIKE '%' || $1 || '%'

                ORDER BY name;
            """, keyword)
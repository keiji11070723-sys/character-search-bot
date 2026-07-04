import asyncpg
from config import DATABASE_URL


class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        """PostgreSQLへ接続"""
        self.pool = await asyncpg.create_pool(DATABASE_URL)

    async def close(self):
        """接続終了"""
        if self.pool:
            await self.pool.close()

    async def initialize(self):
        """テーブル作成"""
        async with self.pool.acquire() as conn:
            with open("database/schema.sql", "r", encoding="utf-8") as f:
                await conn.execute(f.read())

    async def add_character(self, name: str, attribute: str, rarity: str):
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO characters(name, attribute, rarity)
                VALUES($1, $2, $3)
                ON CONFLICT(name) DO NOTHING
                """,
                name,
                attribute,
                rarity,
            )

    async def search_character(self, keyword: str):
        async with self.pool.acquire() as conn:
            return await conn.fetch(
                """
                SELECT name, attribute, rarity
                FROM characters
                WHERE name ILIKE '%' || $1 || '%'
                ORDER BY name
                """,
                keyword,
            )

    async def update_character(
        self,
        old_name: str,
        new_name: str,
        attribute: str,
        rarity: str,
    ):
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                UPDATE characters
                SET
                    name = $2,
                    attribute = $3,
                    rarity = $4
                WHERE name = $1
                """,
                old_name,
                new_name,
                attribute,
                rarity,
            )

    async def delete_character(self, name: str):
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                DELETE FROM characters
                WHERE name = $1
                """,
                name,
            )

    async def get_all(self):
        async with self.pool.acquire() as conn:
            return await conn.fetch(
                """
                SELECT name, attribute, rarity
                FROM characters
                ORDER BY name
                """
            )
import discord
from discord.ext import commands

from config import TOKEN
from database.db import Database


class CharacterBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()

        super().__init__(
            command_prefix="!",
            intents=intents,
        )

        # データベース
        self.db = Database()

    async def setup_hook(self):
        print("データベースへ接続中...")

        # PostgreSQL接続
        await self.db.connect()

        # テーブル作成
        await self.db.initialize()

        print("データベース接続完了")

        # Cog読込
        await self.load_extension("cogs.search")
        await self.load_extension("cogs.admin")

        # SlashCommand同期
        synced = await self.tree.sync()

        print(f"{len(synced)}個のコマンドを同期しました。")

    async def close(self):
        await self.db.close()
        await super().close()


bot = CharacterBot()


@bot.event
async def on_ready():
    print("--------------------------------")
    print(f"ログイン: {bot.user}")
    print("--------------------------------")


bot.run(TOKEN)
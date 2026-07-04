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

        self.db = Database()

    async def setup_hook(self):
        print("データベースへ接続中...")

        await self.db.connect()
        await self.db.initialize()

        print("データベース接続完了")

        await self.load_extension("cogs.search")
        await self.load_extension("cogs.admin")

        # 🔥 ギルド同期（即時反映）
        guild = discord.Object(id=1521974927505227946)
        self.tree.copy_global_to(guild=guild)

        synced = await self.tree.sync(guild=guild)

        print(f"{len(synced)}個のコマンドを同期しました（ギルド同期）")

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
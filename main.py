import discord
from discord.ext import commands

from config import TOKEN
from database.db import Database


class CharacterBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

        self.db = Database()

    async def setup_hook(self):
        print("START SETUP")

        try:
            await self.db.connect()
            await self.db.initialize()
            print("DB OK")

            await self.load_extension("cogs.search")
            await self.load_extension("cogs.admin")
            print("COGS OK")

            guild = discord.Object(id=1521974927505227946)
            self.tree.copy_global_to(guild=guild)

            synced = await self.tree.sync(guild=guild)
            print("SYNC OK:", len(synced))

        except Exception as e:
            print("CRASH:", repr(e))


bot = CharacterBot()


@bot.event
async def on_ready():
    print("LOGIN OK:", bot.user)


bot.run(TOKEN)
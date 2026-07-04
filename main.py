async def setup_hook(self):
    print("start")

    try:
        await self.db.connect()
        await self.db.initialize()

        print("db ok")

        await self.load_extension("cogs.search")
        await self.load_extension("cogs.admin")

        guild = discord.Object(id=1521974927505227946)
        self.tree.copy_global_to(guild=guild)

        synced = await self.tree.sync(guild=guild)

        print("sync ok:", len(synced))

    except Exception as e:
        print("❌ crash:", e)
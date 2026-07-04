async def setup_hook(self):
    print("START BOT")

    try:
        await self.db.connect()
        await self.db.initialize()
        print("DB OK")

        try:
            await self.load_extension("cogs.search")
            await self.load_extension("cogs.admin")
            print("COGS OK")
        except Exception as e:
            print("COG ERROR:", e)

        guild = discord.Object(id=1521974927505227946)
        self.tree.copy_global_to(guild=guild)

        synced = await self.tree.sync(guild=guild)
        print("SYNC OK:", len(synced))

    except Exception as e:
        print("FATAL ERROR:", e)
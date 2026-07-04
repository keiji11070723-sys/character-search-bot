async def setup_hook(self):
    print("DB接続開始")

    await self.db.connect()
    await self.db.initialize()

    print("DB接続完了")

    await self.load_extension("cogs.search")
    await self.load_extension("cogs.admin")

    # 🔥 ギルド同期（確実に表示させる）
    guild = discord.Object(id=1521974927505227946)

    self.tree.clear_commands(guild=guild)  # ←重要（古いコマンド削除）
    self.tree.copy_global_to(guild=guild)

    synced = await self.tree.sync(guild=guild)

    print(f"コマンド同期完了: {len(synced)}個")
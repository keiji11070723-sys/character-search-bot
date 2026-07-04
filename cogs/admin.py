import discord
from discord import app_commands
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 🔥 追加（登録）
    @app_commands.command(name="add", description="キャラクターを追加")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def add(self, interaction: discord.Interaction, 名前: str, 属性: str, レア度: str):

        await self.bot.db.add_character(名前, 属性, レア度)

        await interaction.response.send_message(
            f"✅ 追加しました：{名前}",
            ephemeral=True
        )

    # ✏️ 編集
    @app_commands.command(name="edit", description="キャラクターを編集")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def edit(
        self,
        interaction: discord.Interaction,
        元の名前: str,
        新しい名前: str,
        属性: str,
        レア度: str,
    ):

        await self.bot.db.update_character(
            元の名前,
            新しい名前,
            属性,
            レア度,
        )

        await interaction.response.send_message(
            f"✏️ 編集しました：{元の名前} → {新しい名前}",
            ephemeral=True
        )

    # 🗑 削除
    @app_commands.command(name="delete", description="キャラクターを削除")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def delete(self, interaction: discord.Interaction, 名前: str):

        await self.bot.db.delete_character(名前)

        await interaction.response.send_message(
            f"🗑 削除しました：{名前}",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Admin(bot))
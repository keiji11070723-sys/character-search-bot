import discord
from discord import app_commands
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="追加",
        description="キャラクターを追加します"
    )
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.describe(
        名前="キャラクター名",
        属性="属性",
        レア度="レア度"
    )
    async def add(
        self,
        interaction: discord.Interaction,
        名前: str,
        属性: str,
        レア度: str,
    ):
        await self.bot.db.add_character(
            名前,
            属性,
            レア度,
        )

        await interaction.response.send_message(
            f"✅ **{名前}** を登録しました。",
            ephemeral=True
        )

    @app_commands.command(
        name="編集",
        description="キャラクターを編集します"
    )
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.describe(
        元の名前="変更前の名前",
        新しい名前="変更後の名前",
        属性="属性",
        レア度="レア度"
    )
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
            f"✏️ **{元の名前}** を更新しました。",
            ephemeral=True
        )

    @app_commands.command(
        name="削除",
        description="キャラクターを削除します"
    )
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.describe(
        名前="削除するキャラクター名"
    )
    async def delete(
        self,
        interaction: discord.Interaction,
        名前: str,
    ):
        await self.bot.db.delete_character(名前)

        await interaction.response.send_message(
            f"🗑️ **{名前}** を削除しました。",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Admin(bot))
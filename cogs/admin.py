import discord
from discord import app_commands
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_admin(self, interaction: discord.Interaction) -> bool:
        perms = interaction.user.guild_permissions
        return perms.manage_guild


    @app_commands.command(
        name="追加",
        description="キャラクターを追加します"
    )
    @app_commands.checks.has_permissions(manage_guild=True)
    async def add_character(
        self,
        interaction: discord.Interaction,
        名前: str,
        属性: str,
        レア度: str,
    ):

        await self.bot.db.add_character(
            名前,
            属性,
            レア度
        )

        await interaction.response.send_message(
            f"✅ **{名前}** を登録しました。",
            ephemeral=True
        )


    @app_commands.command(
        name="削除",
        description="キャラクターを削除します"
    )
    @app_commands.checks.has_permissions(manage_guild=True)
    async def delete_character(
        self,
        interaction: discord.Interaction,
        名前: str,
    ):

        await self.bot.db.delete_character(名前)

        await interaction.response.send_message(
            f"🗑️ **{名前}** を削除しました。",
            ephemeral=True
        )


    @app_commands.command(
        name="編集",
        description="キャラクター情報を編集します"
    )
    @app_commands.checks.has_permissions(manage_guild=True)
    async def edit_character(
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


async def setup(bot):
    await bot.add_cog(Admin(bot))
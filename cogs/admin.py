import discord
from discord import app_commands
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_admin(self, interaction: discord.Interaction):
        return interaction.user.guild_permissions.manage_guild

    @app_commands.command(name="add", description="追加")
    async def add(self, interaction, 名前: str, 属性: str, レア度: str):

        if not interaction.user.guild_permissions.manage_guild:
            return await interaction.response.send_message("権限なし", ephemeral=True)

        await self.bot.db.add_character(名前, 属性, レア度)

        await interaction.response.send_message("追加しました", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Admin(bot))
import discord
from discord import app_commands
from discord.ext import commands


class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="検索",
        description="キャラクターを検索します"
    )
    @app_commands.describe(
        名前="検索するキャラクター名"
    )
    async def search(
        self,
        interaction: discord.Interaction,
        名前: str,
    ):
        rows = await self.bot.db.search_character(名前)

        if not rows:
            await interaction.response.send_message(
                "該当するキャラクターは見つかりませんでした。",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="検索結果",
            color=discord.Color.blue()
        )

        for row in rows:
            embed.add_field(
                name=row["name"],
                value=(
                    f"**属性**：{row['attribute']}\n"
                    f"**レア度**：{row['rarity']}"
                ),
                inline=False
            )

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Search(bot))
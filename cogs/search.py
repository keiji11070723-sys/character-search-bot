import discord
from discord import app_commands
from discord.ext import commands


class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="search",
        description="キャラクターを検索します"
    )
    async def search(self, interaction: discord.Interaction, 名前: str):

        try:
            rows = await self.bot.db.search_character(名前)

            if not rows:
                await interaction.response.send_message("見つかりません", ephemeral=True)
                return

            embed = discord.Embed(title="検索結果")

            for r in rows:
                embed.add_field(
                    name=r["name"],
                    value=f"{r['attribute']} / {r['rarity']}",
                    inline=False
                )

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(f"エラー: {e}", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Search(bot))
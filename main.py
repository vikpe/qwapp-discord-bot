import os

import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand, SlashContext

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot)


@slash.slash(name="slashtest")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])


class ServerCog(commands.Cog):
    def __init__(self, bot):
        if not hasattr(bot, "slash"):
            # Creates new SlashCommand instance to bot if bot doesn't have.
            bot.slash = SlashCommand(bot, override_type=True)
        self.bot = bot

    @cog_ext.cog_slash(name="cogtest")
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="embed test")
        await ctx.send(content="test", embeds=[embed])


bot.add_cog(ServerCog(bot))
bot_token = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(bot_token)

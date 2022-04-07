import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot_token = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(bot_token)

import os

from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")


@bot.group()
async def servers(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid server command passed...")


@servers.command(help="List servers")
async def list(ctx) -> None:
    msg = "[list servers]"
    await ctx.send(msg)


@servers.command(help="Start server")
async def start(ctx, aws_region: str) -> None:
    msg = f"[start server in {aws_region}]"
    await ctx.send(msg)


@servers.command(help="Stop server")
async def stop(ctx, server_id: str) -> None:
    msg = f"[stop server by id {server_id}]"
    await ctx.send(msg)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


bot.run(os.environ.get("DISCORD_BOT_TOKEN"))

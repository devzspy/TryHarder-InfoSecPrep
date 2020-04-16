import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def tryharder(ctx):
    channel = ctx.channel
    msg = "https://www.youtube.com/watch?v=6Aw0yOMBbiY"
    await channel.send(msg)

def setup(bot):
    bot.add_command(tryharder)

def teardown(bot):
    bot.remove_command(tryharder)
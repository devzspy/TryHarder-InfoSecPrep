import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def lpeworkshop(ctx):
    channel = ctx.channel
    msg = "https://github.com/sagishahar/lpeworkshop"
    await channel.send(msg)

def setup(bot):
    bot.add_command(lpeworkshop)

def teardown(bot):
    bot.remove_command(lpeworkshop)
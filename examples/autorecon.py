import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def autorecon(ctx):
    channel = ctx.channel
    msg = "https://github.com/Tib3rius/AutoRecon"
    await channel.send(msg)

def setup(bot):
    bot.add_command(autorecon)

def teardown(bot):
    bot.remove_command(autorecon)
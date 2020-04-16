import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def support(ctx):
    channel = ctx.channel
    msg = "In order to get live official support, please visit: https://support.offensive-security.com/, or (#2) Else you can email in: help@offsec.com"
    await channel.send(msg)

def setup(bot):
    bot.add_command(support)

def teardown(bot):
    bot.remove_command(support)
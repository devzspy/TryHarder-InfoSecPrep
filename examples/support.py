import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def support(ctx):
    channel = ctx.channel
    msg = "In order to receive live official support, please visit: https://help.offensive-security.com/hc/en-us, or (#2) Else you can email in: help@offsec.com"
    await channel.send(msg)

def setup(bot):
    bot.add_command(support)

def teardown(bot):
    bot.remove_command(support)
import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def osceexam(ctx):
    channel = ctx.channel
    msg = "https://support.offensive-security.com/osce-exam-guide/"
    await channel.send(msg)

def setup(bot):
    bot.add_command(osceexam)

def teardown(bot):
    bot.remove_command(osceexam)
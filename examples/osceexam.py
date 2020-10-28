import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def osceexam(ctx):
    channel = ctx.channel
    msg = "https://help.offensive-security.com/hc/en-us/articles/360046801331-OSCE-Exam-Guide"
    await channel.send(msg)

def setup(bot):
    bot.add_command(osceexam)

def teardown(bot):
    bot.remove_command(osceexam)
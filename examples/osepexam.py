import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def osepexam(ctx):
    channel = ctx.channel
    msg = "https://help.offensive-security.com/hc/en-us/articles/360050293792-OSEP-Exam-Guide"
    await channel.send(msg)

def setup(bot):
    bot.add_command(osepexam)

def teardown(bot):
    bot.remove_command(osepexam)
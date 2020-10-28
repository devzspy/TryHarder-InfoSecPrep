import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def oseeexam(ctx):
    channel = ctx.channel
    msg = "https://help.offensive-security.com/hc/en-us/articles/360046458732-OSEE-Exam-Guide"
    await channel.send(msg)

def setup(bot):
    bot.add_command(oseeexam)

def teardown(bot):
    bot.remove_command(oseeexam)
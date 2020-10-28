import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def oswpexam(ctx):
    channel = ctx.channel
    msg = "https://help.offensive-security.com/hc/en-us/articles/360046904731-OSWP-Exam-Guide"
    await channel.send(msg)

def setup(bot):
    bot.add_command(oswpexam)

def teardown(bot):
    bot.remove_command(oswpexam)
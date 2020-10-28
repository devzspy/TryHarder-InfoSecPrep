import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def oscpexam(ctx):
    channel = ctx.channel
    msg = "https://help.offensive-security.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide"
    await channel.send(msg)

def setup(bot):
    bot.add_command(oscpexam)

def teardown(bot):
    bot.remove_command(oscpexam)
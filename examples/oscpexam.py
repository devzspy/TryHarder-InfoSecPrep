import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def oscpexam(ctx):
    channel = ctx.channel
    msg = "https://support.offensive-security.com/oscp-exam-guide/"
    await channel.send(msg)

def setup(bot):
    bot.add_command(oscpexam)

def teardown(bot):
    bot.remove_command(oscpexam)
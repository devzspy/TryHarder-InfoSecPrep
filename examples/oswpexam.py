import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def oswpexam(ctx):
    channel = ctx.channel
    msg = "https://support.offensive-security.com/oswp-exam-guide/"
    await channel.send(msg)

def setup(bot):
    bot.add_command(oswpexam)

def teardown(bot):
    bot.remove_command(oswpexam)
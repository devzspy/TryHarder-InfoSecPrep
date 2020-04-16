import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def osweexam(ctx):
    channel = ctx.channel
    msg = "https://support.offensive-security.com/oswe-exam-guide/"
    await channel.send(msg)

def setup(bot):
    bot.add_command(osweexam)

def teardown(bot):
    bot.remove_command(osweexam)
import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def courseleak(ctx):
    userMsg = ctx.message.content()
    channel = bot.get_channel('701897816498241626')
    await channel.send("User Reported: " + userMsg)
    channel = ctx.channel
    await channel.send("We've sent this to offsec staff")

def setup(bot):
    bot.add_command(courseleak)

def teardown(bot):
    bot.remove_command(courseleak)

import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def lmgtfy(ctx):
    template = "https://lmgtfy.com/?q="
    channel = ctx.channel
    userSearch = ctx.message.content.split(" ")
    search = "+".join(userSearch[1:])
    msg = template + search
    await channel.send(msg)

def setup(bot):
    bot.add_command(lmgtfy)

def teardown(bot):
    bot.remove_command(lmgtfy)
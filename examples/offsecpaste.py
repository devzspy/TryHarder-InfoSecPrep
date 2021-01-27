import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def offsecpaste(ctx):
    channel = ctx.channel
    msg = "To avoid spoilers and prevent flooding the chat, please upload your code to https://paste.offsec.com/ and DM me the link"
    await channel.send(msg)

def setup(bot):
    bot.add_command(offsecpaste)

def teardown(bot):
    bot.remove_command(offsecpaste)
import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def cmd(ctx):
    #code

def setup(bot):
    bot.add_command(cmd)

def teardown(bot):
    bot.remove_command(cmd)
import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def kalirevealed(ctx):
    channel = ctx.channel
    msg = "https://www.kali.org/download-kali-linux-revealed-book/"
    await channel.send(msg)

def setup(bot):
    bot.add_command(kalirevealed)

def teardown(bot):
    bot.remove_command(kalirevealed)
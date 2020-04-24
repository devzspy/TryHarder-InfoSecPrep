import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def courseleak(ctx):
    msg = "If you wish to report a leak of an offsec course, please DM either the Discord Staff and we can help you handle it, or the Offsec staff which have the Offensive Security Staff role."
    channel = ctx.channel
    await channel.send(msg)

def setup(bot):
    bot.add_command(courseleak)

def teardown(bot):
    bot.remove_command(courseleak)

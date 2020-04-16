import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def purge(ctx):
    channel = ctx.channel
    fullMsg = ctx.message.content.split(" ")
    if len(fullMsg) <= 2:
        if len(fullMsg) == 1:
            limit = 200
        else:
            limit = int(fullMsg[1])+1
        deleted = await channel.purge(limit=limit)
    msg = ctx.message
    await msg.delete()

def setup(bot):
    bot.add_command(purge)

def teardown(bot):
    bot.remove_command(purge)
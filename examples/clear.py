import discord
from discord.ext import commands
from builtins import bot
from datetime import datetime,timedelta

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def clear(ctx):
    fullMsg = ctx.message.content.split(" ")
    channel = ctx.channel
    if len(fullMsg) == 2:
        user = fullMsg[1].replace("<", "").replace("@", "").replace(">", "")
        messages = []
        counter = 0
        max_days = 13
        max_days_ago = datetime.now() - timedelta(days=max_days)
        async for message in channel.history(limit=500,after=max_days_ago):
            if counter == 100:
                break
            if user == str(message.author.id):
                messages.append(message)
                counter += 1
        deleted = await channel.delete_messages(messages)
    elif len(fullMsg) == 3:
        user = fullMsg[1].replace("<", "").replace("@", "").replace(">", "")
        limit = int(fullMsg[2])
        messages = []
        counter = 0
        max_days = 13
        max_days_ago = datetime.now() - timedelta(days=max_days)
        async for message in channel.history(limit=500,after=max_days_ago):
            if counter == limit:
                break
            if user == str(message.author.id):
                messages.append(message)
                counter += 1
        deleted = await channel.delete_messages(messages)        
    msg = ctx.message
    await msg.delete()


def setup(bot):
    bot.add_command(clear)

def teardown(bot):
    bot.remove_command(clear)
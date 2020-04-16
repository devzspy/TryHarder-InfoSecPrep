import discord
from discord.ext import tasks
from builtins import bot

@tasks.loop(seconds=25.0)
async def postWarning():
    server = bot.get_guild(427589708290457630)
    channel = discord.utils.get(server.channels, name="ephemeral-chat")
    await channel.send("WARNING: The channel will be wiped within 1 minute.") 

    #for role in server.roles:
    #    if role.name == "Muted" or role.name == "TryHarder":
    #        pass
    #    else:
    #        overwrite = discord.PermissionOverwrite()
    #        overwrite.send_messages = False
    #        await channel.set_permissions(role, overwrite=overwrite)

    await channel.send('This channel is now in read-only mode.')

@tasks.loop(seconds=30.0)
async def deleteMessages():
    server = bot.get_guild(427589708290457630)
    channel = discord.utils.get(server.channels, name="ephemeral-chat")
    keepMsg = await channel.fetch_message(695703957657485322)

    counter = 0
    async for message in channel.history(after=keepMsg):
        counter += 1

    totalLoops = int(counter/100.0+1)

    await channel.send('Clearing messages...')

    deleted = await channel.purge(oldest_first=True, after=keepMsg)

    print(len(deleted))

    #await channel.send("Statistics: Deleted %s messages in the past hour." % counter)

    #for role in server.roles:
    #    if role.name == "Muted" or role.name == "TryHarder":
    #        pass
    #    else:
    #        overwrite = discord.PermissionOverwrite()
    #        overwrite.send_messages = True
    #        await channel.set_permissions(role, overwrite=overwrite)

    await channel.send('You may speak again.')

def setup(bot):
    print("ephemeral module loaded")
    postWarning.start()
    deleteMessages.start()

def teardown(bot):
    print("ephemeral module unloaded")
    postWarning.cancel()
    deleteMessages.cancel()

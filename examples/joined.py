import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def joined(ctx):
    msg = ctx.message.content.split(" ")
    server = ctx.guild
    cmdChan = discord.utils.get(server.channels, name="bot-commands")
    staffCmdChan = discord.utils.get(server.channels, name="staff-commands")
    if ctx.channel == cmdChan:
        user = ctx.author.id
        member = server.get_member(user)
        mention = member.mention
        joinedOn = member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
        await cmdChan.send("%s joined the server on %s" % (mention, joinedOn))
    elif ctx.channel == staffCmdChan:
        if len(msg) == 2:
            user = msg[1].replace("<", "").replace("@", "").replace("!","").replace(">", "")
            member = server.get_member(int(user))
            mention = member.mention
            joinedOn = member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
            await staffCmdChan.send("%s joined the server on %s" % (mention, joinedOn))

def setup(bot):
    bot.add_command(joined)

def teardown(bot):
    bot.remove_command(joined)
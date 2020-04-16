import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def echo(ctx):
    server = ctx.guild
    adminChannel = discord.utils.get(server.channels, name="staff-commands")
    if ctx.channel == adminChannel:
        fullMsg = ctx.message.content.split(" ")
        if len(fullMsg) >= 3:
            channel = fullMsg[1].replace("<", "").replace("#", "").replace(">", "")
            channel = bot.get_channel(int(channel))
            msg = " "
            msg = msg.join(fullMsg[2:])
            await channel.send(msg)


def setup(bot):
    bot.add_command(echo)

def teardown(bot):
    bot.remove_command(echo)
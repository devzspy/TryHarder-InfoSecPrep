import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def multipin(ctx):
    server = ctx.guild
    adminChannel = discord.utils.get(server.channels, name="staff-commands")
    if ctx.channel == adminChannel:
        fullMsg = ctx.message.content.split(" ")
        if len(fullMsg) >= 3:
            channels = []
            for i,w in  enumerate(fullMsg[1:]):
                if w.startswith("<#"):
                    channel = w.replace("<", "").replace("#", "").replace(">", "")
                    channel = bot.get_channel(int(channel))
                    channels.append(channel)
                else:
                    pinMsg=fullMsg[i+1:]
                    break
                    
            
            for channel in  channels:
                msg = " "
                msg = msg.join(pinMsg)
                msg = await channel.send(msg)
                await discord.Message.pin(msg)


def setup(bot):
    bot.add_command(multipin)

def teardown(bot):
    bot.remove_command(multipin)

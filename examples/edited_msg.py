import discord
from discord.ext import commands
from builtins import bot

'''
Before:
-------
<Message id=674689532464988180 channel=<TextChannel id=674682927187099648 name='test' position=51 nsfw=False news=False category_id=601816009753624614> 
type=<MessageType.default: 0> author=<Member id=96269737343844352 name='FalconSpy' discriminator='0512' bot=False nick=None guild=<Guild id=427589708290457630 
name='InfoSec Prep' shard_id=None chunked=True member_count=4935>>>

after:
------
<Message id=674689532464988180 channel=<TextChannel id=674682927187099648 name='test' position=51 nsfw=False news=False category_id=601816009753624614> 
type=<MessageType.default: 0> author=<Member id=96269737343844352 name='FalconSpy' discriminator='0512' bot=False nick=None guild=<Guild id=427589708290457630 
name='InfoSec Prep' shard_id=None chunked=True member_count=4935>>>
'''

@bot.event
async def on_message_edit(before, after):
    ctx = before
    server = ctx.guild
    logChannel = discord.utils.get(server.channels, name="message-audit-log")
    if ctx.author.bot and ctx.channel == logChannel:
        pass
    else:
        msgEditedChannel = ctx.channel
        title = "Message edited in %s" % msgEditedChannel
        embed=discord.Embed(title=title, color=0xffff00)
        embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/1428/1428326.png")
        embed.add_field(name="Message by", value=ctx.author, inline=False)
        await logChannel.send(embed=embed)

        msg = "**Before:**\n"
        msg += before.content
        msg += "\n\n"
        msg += "**After:**\n"
        msg += after.content
        msg += "\n----------------------------------------"

        await logChannel.send(msg)

def setup(bot):
    print("Edited msgs module loaded")

def teardown(bot):
    print("Edited msgs module removed")
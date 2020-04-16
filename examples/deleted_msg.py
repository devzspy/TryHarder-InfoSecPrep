import discord
from discord.ext import commands
from builtins import bot
from datetime import datetime,timezone,timedelta

'''
<AuditLogEntry id=673793139038879744 action=AuditLogAction.message_delete user=<Member id=96269737343844352 name='FalconSpy' discriminator='0512' 
bot=False nick=None guild=<Guild id=427589708290457630 name='InfoSec Prep' shard_id=None chunked=True member_count=4889>>>
2020-02-03 08:09:36.228000
'''

@bot.event
async def on_message_delete(ctx):
    currentDateTime = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")
    server = ctx.guild
    logChannel = discord.utils.get(server.channels, name="message-audit-log")
    if ctx.author == 'TryHarder#6562' and ctx.channel == logChannel:
        pass
    else:
        msgDeletedChannel = ctx.channel
        async for entry in server.audit_logs(action=discord.AuditLogAction.message_delete, limit=1):
            title = "Message deleted in %s" % msgDeletedChannel
            embed=discord.Embed(title=title, color=0xff0000)
            embed.set_thumbnail(url="https://img.icons8.com/material-two-tone/452/deleted-message.png")
            embed.add_field(name="Message by", value=ctx.author, inline=True)
            currentDateTime = datetime.strptime(currentDateTime, "%Y-%m-%d %H:%M:%S.%f")
            if (currentDateTime - entry.created_at).total_seconds() > 120:
                embed.add_field(name="Deleted By", value=ctx.author, inline=True)
            else:
                embed.add_field(name="Deleted By", value=entry.user, inline=True)
            await logChannel.send(embed=embed)
            await logChannel.send("**Message**: \n" + ctx.content + "\n----------------------------------------")

@bot.event
async def on_bulk_message_delete(ctx):
    pass

def setup(bot):
    print("Deleted msgs module loaded")

def teardown(bot):
    print("Deleted msgs module removed")
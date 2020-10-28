import discord
from discord.ext import commands
from builtins import bot
from datetime import datetime,timezone,timedelta

'''
payload = 

<RawReactionActionEvent message_id=695502056106098690 user_id=96269737343844352 channel_id=695479820506890340 guild_id=427589708290457630 
emoji=<PartialEmoji animated=False name='oscp' id=651326976799277076>>

<RawReactionActionEvent message_id=695480723695730718 user_id=96269737343844352 channel_id=695479820506890340 guild_id=427589708290457630 
emoji=<PartialEmoji animated=False name='osce' id=651327042469625856>>

<RawReactionActionEvent message_id=695480723695730718 user_id=96269737343844352 channel_id=695479820506890340 guild_id=427589708290457630 
emoji=<PartialEmoji animated=False name='oswe' id=651327013440716820>>

<RawReactionActionEvent message_id=695480723695730718 user_id=96269737343844352 channel_id=695479820506890340 guild_id=427589708290457630 
emoji=<PartialEmoji animated=False name='oswp' id=651327095862984715>>
'''

'''
    print(payload)
    print(payload.channel_id)
    print(payload.emoji.name)
    print(bot.get_channel(payload.channel_id))
    print(bot.get_guild(payload.guild_id))
    server = bot.get_guild(payload.guild_id)
    channel = discord.utils.get(server.channels, name="role-test")
    print(channel)
'''

@bot.event
async def on_raw_reaction_add(payload):
    server = bot.get_guild(payload.guild_id)
    member = server.get_member(payload.user_id)
    userMention = member.mention
    studentChannel = discord.utils.get(server.channels, name="student-roles")
    channel = bot.get_channel(payload.channel_id)
    reaction = payload.emoji.name
    if studentChannel == channel:
        if reaction == "oscp" or reaction == "oswp" or reaction == "oswe" or reaction == "osce" or reaction == "osep" or reaction == "wapt":
            role = discord.utils.get(server.roles, name="%s Student" % reaction.upper())
            roleMention = role.mention
            await member.add_roles(role)
            delmsg = await channel.send("%s - you have been added to %s" % (userMention, roleMention))  
            await delmsg.delete(delay=10.0)

@bot.event
async def on_raw_reaction_remove(payload):
    server = bot.get_guild(payload.guild_id)
    member = server.get_member(payload.user_id)
    userMention = member.mention
    studentChannel = discord.utils.get(server.channels, name="student-roles")
    channel = bot.get_channel(payload.channel_id)
    reaction = payload.emoji.name
    if studentChannel == channel:
        if reaction == "oscp" or reaction == "oswp" or reaction == "oswe" or reaction == "osce" or reaction == "osep" or reaction == "wapt":
            role = discord.utils.get(server.roles, name="%s Student" % reaction.upper())
            roleMention = role.mention
            await member.remove_roles(role) 
            delmsg = await channel.send("%s - you have been removed from %s" % (userMention, roleMention))
            await delmsg.delete(delay=10.0)

def setup(bot):
    print("student v2 module loaded")

def teardown(bot):
    print("student v2 module removed")
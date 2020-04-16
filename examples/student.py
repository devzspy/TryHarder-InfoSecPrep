import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def oscp(ctx): 
    user = ctx.author.id
    server = ctx.guild
    channel = discord.utils.get(server.channels, name="student-roles")
    if ctx.channel == channel:
        member = server.get_member(user)
        userMention = member.mention
        role = discord.utils.get(server.roles, name="OSCP Student")
        roleMention = role.mention
        await member.add_roles(role) 
        await channel.send("%s - you have been added to %s" % (userMention, roleMention))   

@commands.command()
async def oswe(ctx):
    user = ctx.author.id 
    server = ctx.guild
    channel = discord.utils.get(server.channels, name="student-roles")
    if ctx.channel == channel:
        member = server.get_member(user)
        userMention = member.mention
        role = discord.utils.get(server.roles, name="OSWE Student")
        roleMention = role.mention
        await member.add_roles(role)    
        await channel.send("%s - you have been added to %s" % (userMention, roleMention))   

@commands.command()
async def osce(ctx):
    user = ctx.author.id  
    server = ctx.guild
    channel = discord.utils.get(server.channels, name="student-roles")
    if ctx.channel == channel:
        member = server.get_member(user)
        userMention = member.mention
        role = discord.utils.get(server.roles, name="OSCE Student")
        roleMention = role.mention
        await member.add_roles(role)             
        await channel.send("%s - you have been added to %s" % (userMention, roleMention))

@commands.command()
async def oswp(ctx): 
    user = ctx.author.id
    server = ctx.guild
    channel = discord.utils.get(server.channels, name="student-roles")
    if ctx.channel == channel:
        member = server.get_member(user)
        userMention = member.mention
        role = discord.utils.get(server.roles, name="OSWP Student")
        roleMention = role.mention
        await member.add_roles(role) 
        await channel.send("%s - you have been added to %s" % (userMention, roleMention))   

@commands.command()
async def wapt(ctx): 
    user = ctx.author.id
    server = ctx.guild
    channel = discord.utils.get(server.channels, name="student-roles")
    if ctx.channel == channel:
        member = server.get_member(user)
        userMention = member.mention
        role = discord.utils.get(server.roles, name="WAPT Student")
        roleMention = role.mention
        await member.add_roles(role) 
        await channel.send("%s - you have been added to %s" % (userMention, roleMention))         


def setup(bot):
    bot.add_command(oscp)
    bot.add_command(oswe)
    bot.add_command(osce)
    bot.add_command(oswp)
    bot.add_command(wapt)

def teardown(bot):
    bot.remove_command(oscp)
    bot.remove_command(oswe)
    bot.remove_command(osce)
    bot.remove_command(oswp)
    bot.remove_command(wapt)
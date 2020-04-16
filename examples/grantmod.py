import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def grantmod(ctx):
    server = ctx.guild
    message = ctx.message.content.split(" ")
    channel = discord.utils.get(server.channels, name="staff-commands")
    if ctx.channel == channel:
        if len(message) == 2: 
            assignedRole = message[1]
            if assignedRole == "oscp":
                certified = discord.utils.get(server.roles, name="OSCP Certified")
                users = certified.members
                role = discord.utils.get(server.roles, name="OSCP Certified Mod")
                await channel.send("There are %s users being assigned the role. Please wait... " % len(users))
                await addRole(ctx, role, users)
            elif assignedRole == "oswp":
                certified = discord.utils.get(server.roles, name="OSWP Certified")
                users = certified.members
                role = discord.utils.get(server.roles, name="OSWP Certified Mod")
                await channel.send("There are %s users being assigned the role. Please wait... " % len(users))
                await addRole(ctx, role, users)
            elif assignedRole == "oswe":
                certified = discord.utils.get(server.roles, name="OSWE Certified")
                users = certified.members
                role = discord.utils.get(server.roles, name="OSWE Certified Mod")
                await channel.send("There are %s users being assigned the role. Please wait... " % len(users))
                await addRole(ctx, role, users)
            elif assignedRole == "osce":
                certified= discord.utils.get(server.roles, name="OSCE Certified")
                users = certified.members
                role = discord.utils.get(server.roles, name="OSCE Certified Mod")
                await channel.send("There are %s users being assigned the role. Please wait... " % len(users))
                await addRole(ctx, role, users)
        
        await channel.send("All users belonging to %s have been given mod role" % assignedRole)

async def addRole(ctx, role, users):
    for user in users:
        await user.add_roles(role)

def setup(bot):
    bot.add_command(grantmod)

def teardown(bot):
    bot.remove_command(grantmod)
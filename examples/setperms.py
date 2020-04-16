import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator')
async def setperms(ctx):
    server = ctx.guild
    channel = discord.utils.get(server.channels, name="student-roles")

    for role in server.roles:
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.add_reactions = False
        await channel.set_permissions(role, overwrite=overwrite)

def setup(bot):
    bot.add_command(setperms)

def teardown(bot):
    bot.remove_command(setperms)
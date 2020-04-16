import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def mute(ctx, member: discord.Member):
    fullMsg = ctx.message.content.split(" ")
    server = ctx.guild
    cmdChan = discord.utils.get(server.channels, name="staff-commands")
    if ctx.channel == cmdChan:
        if len(fullMsg) == 2:
            role = discord.utils.get(server.roles, name="Muted")
            await member.add_roles(role)

def setup(bot):
    bot.add_command(mute)

def teardown(bot):
    bot.remove_command(mute)
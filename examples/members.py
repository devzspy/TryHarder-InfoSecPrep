import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def members(ctx):
    server = ctx.guild
    cmdChan = discord.utils.get(server.channels, name="bot-commands")
    members = server.member_count
    msg = str(members)
    embed=discord.Embed(title="Total Members", description=members, color=0x00ff00)
    await cmdChan.send(embed=embed)

def setup(bot):
    bot.add_command(members)

def teardown(bot):
    bot.remove_command(members)
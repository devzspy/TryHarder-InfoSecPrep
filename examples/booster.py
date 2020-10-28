import discord
from discord.ext import commands
from builtins import bot

@bot.event
async def on_member_update(before, after):
    if before.premium_since is None and after.premium_since is not None:
        server = after.guild
        channel = discord.utils.get(server.channels, name="server-boosters")
        user = after
        msg = "Thanks for boosting the server %s" % user.mention
        await channel.send(msg)

def setup(bot):
    print("Nitrobooster module loaded")

def teardown(bot):
    print("Nitrobooster module removed")
import discord
from discord.ext import commands
from builtins import bot

@bot.command()
async def hello2(ctx):
    await ctx.send("hello2 %s" % ctx.author.name)
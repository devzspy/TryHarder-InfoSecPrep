import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    print(ctx)
    print({0})
    # await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

bot.run('NTczNzY2MDE0NjE4MzA0NTEy.XVobtw.XVKyc3AjC8yDH1-jliQiv5-WkQE')

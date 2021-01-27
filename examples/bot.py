import discord
from discord.ext import commands
import builtins
import pymysql
import asyncio
from datetime import datetime,time
import pkg_resources

intents = discord.Intents.default() #Change this to have whatever intents you wish

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix=('?', '!'), description=description, intents=intents)
bot.remove_command('help')

builtins.bot = bot

startup_extensions = [
    "welcome",
    "rules",
    "members",
    "stats",
    #"student",
    "studentv2",
    "mute",
    "help",
    "purge",
    "joined",
    "verify",
    "support",
    "echo",
    "tryharder",
    "autorecon",
    "oscpexam",
    "osweexam",
    "osceexam",
    "oswpexam",
    "osepexam",
    "oseeexam",
    "deleted_msg",
    "edited_msg",
    "lmgtfy",
    "lpeworkshop",
    #"oscp-flag",
    "booster",
    'kalirevealed',
    'offsecpaste'
]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('version: ' + discord.__version__)
    print('------')

def is_me(ctx):
    return ctx.author.id == 96269737343844352

@bot.command()
@commands.check(is_me)
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    channel = ctx.channel
    await channel.send("{} loaded.".format(extension_name))

@bot.command()
@commands.check(is_me)
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    channel = ctx.channel
    await channel.send("{} unloaded.".format(extension_name))

@bot.command()
@commands.check(is_me)
async def reload(ctx, extension_name : str):
    """reloads extension."""
    bot.unload_extension(extension_name)
    bot.load_extension(extension_name)

if __name__ == "__main__":
    print("\n")
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loaded extension {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run('Insert Token Here')

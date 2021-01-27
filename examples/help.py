import discord
from discord.ext import commands
from builtins import bot


def adminCmds():
    embed = discord.Embed(title="Administrative Commands", description="User level commands are included", color=0x07fcf0)
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/RyBiRwUtq8VqdDb6Sm77J303UEziO55Ujqu8FaRCfQ4/https/i.imgur.com/JsgxK3Y.png")
    embed.add_field(name="?welcome", value="Sets the welcome message in <#613636504782110724>. Must be executed in <#630675224383455254>.", inline=False)
    embed.add_field(name="?examrules", value="Sets the exam rules in <#613630998718185472>. Must be executed in <#630675224383455254>.", inline=False)
    embed.add_field(name="?rules", value="Sets the general rules in <#613630998718185472>. Must be executed in <#630675224383455254>.", inline=False)
    embed.add_field(name="?mute [@<username>]", value="Makes it so a user is unable to talk on the server. Must be @mentioned. Must be executed in <#630675224383455254>.", inline=False)
    #embed.add_field(name="?clear [@<username>] [limit] (Optional)", value="Removes last 100 messages from user in specific channel by default. You can also specify a limit. Must be @mentioned", inline=False)
    embed.add_field(name="?purge [limit] (Optional)", value="Will remove the last 200 messages in a channel by default if no limit specified. Use with caution.", inline=False)
    embed.add_field(name="?joined [@<username>]", value="Will output when the user joined the server. Must be executed in <#630675224383455254>. Different from user ?joined. See user notes.", inline=False)
    embed.add_field(name="?verify [@<username>]", value="Use command in verification channels only. Will revoke student role and grant certified role. Roles determined based on verification channel.", inline=False)
    embed.add_field(name="?echo [#channel] [msg]", value="Makes the bot send a message to specified channel. Must be executed in <#630675224383455254>.", inline=False)
    return embed

def userCmds():
    embed = discord.Embed(title="User Commands", color=0x07fcf0)
    embed.add_field(name="?help", value="Displays this menu", inline=False)
    embed.add_field(name="?members", value="Displays the total number of users on the server", inline=False)
    embed.add_field(name="?stats", value="Displays stats for each student role and certified users", inline=False)
    embed.add_field(name="?joined", value="Displays when you joined the server.", inline=False)
    embed.add_field(name="?support", value="Global command. Provides official OffSec support channels.", inline=False)
    embed.add_field(name="?tryharder", value="Global command. Try Harder", inline=False)
    embed.add_field(name="?autorecon", value="Global command. Spits out the URL to AutoRecon GitHub Repo", inline=False)
    embed.add_field(name="?oscpexam", value="Spits out the URL to OSCP Exam guide. Global command - works anywhere in server. ", inline=False)
    embed.add_field(name="?osweexam", value="Spits out the URL to OSWE Exam guide. Global command - works anywhere in server. ", inline=False)
    embed.add_field(name="?osceexam", value="Spits out the URL to OSCE Exam guide. Global command - works anywhere in server. ", inline=False)
    embed.add_field(name="?oswpexam", value="Spits out the URL to OSWP Exam guide. Global command - works anywhere in server. ", inline=False)
    embed.add_field(name="?osepexam", value="Spits out the URL to OSEP Exam guide. Global command - works anywhere in server. ", inline=False)
    embed.add_field(name="?oseeexam", value="Spits out the URL to OSEE Exam guide. Global command - works anywhere in server. ", inline=False)
    embed.add_field(name="?offsecpaste", value="Spits out a courtesy note and the URL to offsec privatebin. Global command - works anywhere in server. ", inline=False)
    embed.add_field(name="?kalirevealed", value="Spits out the URL to the Kali Revealed page. Global command - works anywhere in server. ", inline=False)
    embed.add_field(name="?lmgtfy [<stuff to search for>]", value="Used for snarky response on how to search stuff. Global command - works anywhere in the server.", inline=False)
    embed.add_field(name="?lpeworkshop", value="Spits out Windows/Linux Local Priv Esc Workshop link. Global command - works anywhere in the server.", inline=False)
    return embed

@commands.command()
async def help(ctx):
    server = ctx.guild
    botChannel = discord.utils.get(server.channels, name="bot-commands")
    adminChannel = discord.utils.get(server.channels, name="staff-commands")
    if ctx.channel == botChannel:
        embed = userCmds()
        await botChannel.send(embed=embed)
    elif ctx.channel == adminChannel:
        embed = adminCmds()
        await adminChannel.send(embed=embed)
        embed = userCmds()
        await adminChannel.send(embed=embed)

def setup(bot):
    bot.add_command(help)

def teardown(bot):
    bot.remove_command(help)
import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def welcome(ctx):
    cmdChan = discord.utils.get(server.channels, name="staff-commands")
    sendChan = discord.utils.get(server.channels, name="welcome")
    if ctx.channel == cmdChan:
        await cmdChan.send("Welcome message posted. Please note this is a static message and requires updating in bot src code.")
        embed = discord.Embed(title="Welcome to InfoSec Prep", description="This server was created in order for all the students attempting to acquire the various Offensive Security certifications to have a place to discuss; the exercises, lab machines, pass-fail experiences, and anything InfoSec related. That being said, please review the rules, which can be found in <#613630998718185472>.", color=0x00ff00)
        embed.add_field(name="Invite link for your friends:", value="https://discord.gg/RRgKaep", inline=False)
        embed.set_image(url="https://www.offensive-security.com/wp-content/uploads/2015/06/Offsec-Red-Site-Logo-2015-600x180.png")
        await sendChan.send(embed=embed)

def setup(bot):
    bot.add_command(welcome)

def teardown(bot):
    bot.remove_command(welcome)
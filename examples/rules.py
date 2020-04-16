import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def examrules(ctx):
    cmdChan = discord.utils.get(server.channels, name="staff-commands")
    sendChan = discord.utils.get(server.channels, name="rules")
    if ctx.channel == cmdChan:
        await cmdChan.send("Exam rules posted. Please note this is a static message and requires updating in bot src code.")
        embed = discord.Embed(title="Exam Rules", color=0xff0000)
        embed.add_field(name="Do not ask questions", value="Users found asking questions during the exam will receive one warning. Should they continue to ask questions, they will be banned and Offensive Security will be notified.", inline=False)
        await sendChan.send(embed=embed)

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def rules(ctx):
    cmdChan = discord.utils.get(server.channels, name="staff-commands")
    sendChan = discord.utils.get(server.channels, name="rules")
    if ctx.channel == cmdChan:
        await cmdChan.send("Server rules posted. Please note this is a static message and requires updating in bot src code.")
        embed=discord.Embed(title="Server Rules", description="", color=0x0080ff)
        embed.add_field(name="1. No spoilers" , value="We ask our users to not post anything that may spoil a host in the labs or ruin an exercise.", inline=False)
        embed.add_field(name="2. No irrelevant discussions/offtopic chatter", value="Please keep all topics relevant to the channel you are speaking in. You may post just about anything you want in <#427589708290457632>.", inline=False)
        embed.add_field(name="3. NO DIRECT QUESTIONS ON MACHINES" , value="Please do not ask questions specific to any lab machine. You may ask for help regarding a machine and take it to a Direct Message. For example: Can someone help me with priv esc on Alice", inline=False)
        embed.add_field(name="4. No unsolicited DMs", value="Please do not DM other users without their consent. Should you receive unsolicited DMs please notify server staff if you see fit.", inline=False)
        embed.add_field(name="5. No shitposting/memes" , value="You may post whatever meme/shipost you'd like in <#620354876555264000>. An occaisonal post anywhere else is fine, but please try to limit it severely.", inline=False)
        embed.add_field(name="6. Try harder" , value="Did you try hard enough?", inline=False)
        embed.add_field(name="7. No NSFW/NSFL content", value="We have individuals of all ages. Do not post anything on here that could get another individual potentially fired at their work environment." , inline=False)
        embed.add_field(name="8. Do not post Active HTB Machine Flags" , value="Any user found posting flags for active machines on HTB will be removed. Should we also see that your Discord ID matches your HTB ID we will notify @HTB Ambassador of your infractions.", inline=False)
        embed.add_field(name="9. Do not ignore the rules", value="People blatantly ignoring the rules will either get warned or kicked out from the server", inline=False)
        embed.set_image(url="https://www.offensive-security.com/wp-content/uploads/2015/06/Offsec-Red-Site-Logo-2015-600x180.png")
        await sendChan.send(embed=embed)

def setup(bot):
    bot.add_command(examrules)
    bot.add_command(rules)

def teardown(bot):
    bot.remove_command(examrules)
    bot.remove_command(rules)
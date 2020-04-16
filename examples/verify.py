import discord
from discord.ext import commands
from builtins import bot

@commands.command()
@commands.has_any_role('Administrator', 'Moderator')
async def verify(ctx, member: discord.Member):
    server = ctx.guild
    channel = ctx.channel
    message = ctx.message.content.split(" ")

    oscp_verify_channel = discord.utils.get(server.channels, name="oscp-verification")
    oswe_verify_channel = discord.utils.get(server.channels, name="oswe-verification")
    osce_verify_channel = discord.utils.get(server.channels, name="osce-verification")
    oswp_verify_channel = discord.utils.get(server.channels, name="oswp-verification")

    oscp_certified_channel = discord.utils.get(server.channels, name="haxx0rz-only")
    oswe_certified_channel = discord.utils.get(server.channels, name="webhaxx0rz-only")
    osce_certified_channel = discord.utils.get(server.channels, name="os-misconfig-master")
    oswp_certified_channel = discord.utils.get(server.channels, name="got-wifu")

    if len(message) == 2:
        userMention = member.mention
        if channel == oscp_verify_channel:
            studentRole = discord.utils.get(server.roles, name="OSCP Student")
            studentMention = studentRole.mention
            verifyRole = discord.utils.get(server.roles, name="OSCP Certified")
            verifyMention = verifyRole.mention
            modRole = discord.utils.get(server.roles, name="OSCP Certified Mod")
            modMention = modRole.mention
            await member.remove_roles(studentRole, reason="Student verified OSCP Certification")
            await member.add_roles(verifyRole)
            await member.add_roles(modRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s & %s role" % (userMention, studentMention, verifyMention, modMention))
            await oscp_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden.\n\nYou have mod permissions to the OSCP Course Section. Do not abuse it." % (userMention))

        elif channel == oswe_verify_channel:
            studentRole = discord.utils.get(server.roles, name="OSWE Student")
            studentMention = studentRole.mention
            verifyRole = discord.utils.get(server.roles, name="OSWE Certified")
            verifyMention = verifyRole.mention
            modRole = discord.utils.get(server.roles, name="OSWE Certified Mod")
            modMention = modRole.mention
            await member.remove_roles(studentRole, reason="Student verified OSWE Certification")
            await member.add_roles(verifyRole)
            await member.add_roles(modRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s & %s role" % (userMention, studentMention, verifyMention, modMention))
            await oswe_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden.\n\nYou have mod permissions to the OSWE Course Section. Do not abuse it." % (userMention))

        elif channel == osce_verify_channel:
            studentRole = discord.utils.get(server.roles, name="OSCE Student")
            studentMention = studentRole.mention
            verifyRole = discord.utils.get(server.roles, name="OSCE Certified")
            verifyMention = verifyRole.mention
            modRole = discord.utils.get(server.roles, name="OSCE Certified Mod")
            modMention = modRole.mention
            await member.remove_roles(studentRole, reason="Student verified OSCE Certification")
            await member.add_roles(verifyRole)
            await member.add_roles(modRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s & %s role" % (userMention, studentMention, verifyMention, modMention))
            await osce_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden.\n\nYou have mod permissions to the OSCE Course Section. Do not abuse it." % (userMention))

        elif channel == oswp_verify_channel:
            studentRole = discord.utils.get(server.roles, name="OSWP Student")
            studentMention = studentRole.mention
            verifyRole = discord.utils.get(server.roles, name="OSWP Certified")
            verifyMention = verifyRole.mention
            modRole = discord.utils.get(server.roles, name="OSWP Certified Mod")
            modMention = modRole.mention
            await member.remove_roles(studentRole, reason="Student verified OSWP Certification")
            await member.add_roles(verifyRole)
            await member.add_roles(modRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s & %s role" % (userMention, studentMention, verifyMention, modMention))
            await oswp_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden.\n\nYou have mod permissions to the OSWP Course Section. Do not abuse it." % (userMention))


def setup(bot):
    bot.add_command(verify)

def teardown(bot):
    bot.remove_command(verify)
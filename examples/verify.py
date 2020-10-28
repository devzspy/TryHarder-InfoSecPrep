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
    osep_verify_channel = discord.utils.get(server.channels, name="osep-verification")
    oswe_verify_channel = discord.utils.get(server.channels, name="oswe-verification")
    osce_verify_channel = discord.utils.get(server.channels, name="osce-verification")
    oswp_verify_channel = discord.utils.get(server.channels, name="oswp-verification")

    oscp_certified_channel = discord.utils.get(server.channels, name="haxx0rz-only")
    osep_certified_channel = discord.utils.get(server.channels, name="evasion-master")
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
            await member.remove_roles(studentRole, reason="Student verified OSCP Certification")
            await member.add_roles(verifyRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s" % (userMention, studentMention, verifyMention))
            await oscp_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden." % (userMention))

        elif channel == osep_verify_channel:
            studentRole = discord.utils.get(server.roles, name="OSEP Student")
            studentMention = studentRole.mention
            verifyRole = discord.utils.get(server.roles, name="OSEP Certified")
            verifyMention = verifyRole.mention
            await member.remove_roles(studentRole, reason="Student verified OSEP Certification")
            await member.add_roles(verifyRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s" % (userMention, studentMention, verifyMention))
            await osep_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden." % (userMention))           

        elif channel == oswe_verify_channel:
            studentRole = discord.utils.get(server.roles, name="OSWE Student")
            studentMention = studentRole.mention
            verifyRole = discord.utils.get(server.roles, name="OSWE Certified")
            verifyMention = verifyRole.mention
            await member.remove_roles(studentRole, reason="Student verified OSWE Certification")
            await member.add_roles(verifyRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s" % (userMention, studentMention, verifyMention))
            await oswe_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden." % (userMention))

        elif channel == osce_verify_channel:
            studentRole = discord.utils.get(server.roles, name="OSCE Student")
            studentMention = studentRole.mention
            verifyRole = discord.utils.get(server.roles, name="OSCE Certified")
            verifyMention = verifyRole.mention
            await member.remove_roles(studentRole, reason="Student verified OSCE Certification")
            await member.add_roles(verifyRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s" % (userMention, studentMention, verifyMention))
            await osce_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden." % (userMention))

        elif channel == oswp_verify_channel:
            studentRole = discord.utils.get(server.roles, name="OSWP Student")
            studentMention = studentRole.mention
            verifyRole = discord.utils.get(server.roles, name="OSWP Certified")
            verifyMention = verifyRole.mention
            await member.remove_roles(studentRole, reason="Student verified OSWP Certification")
            await member.add_roles(verifyRole)
            await channel.send("%s has been verified. Revoked: %s role | Added: %s" % (userMention, studentMention, verifyMention))
            await oswp_certified_channel.send("Welcome %s\n\nDiscussion of exam hosts is forbidden." % (userMention))


def setup(bot):
    bot.add_command(verify)

def teardown(bot):
    bot.remove_command(verify)
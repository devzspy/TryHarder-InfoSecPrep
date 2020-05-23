import discord
from discord.ext import commands
from builtins import bot

@commands.command()
async def stats(ctx):
    server = ctx.guild
    channel = discord.utils.get(server.channels, name="bot-commands")
    if ctx.channel == channel: 
        totalMembers = str(server.member_count)
        oscp_S_Role = discord.utils.get(server.roles, name="OSCP Student")
        oswe_S_Role = discord.utils.get(server.roles, name="OSWE Student")
        osce_S_Role = discord.utils.get(server.roles, name="OSCE Student")
        oswp_S_Role = discord.utils.get(server.roles, name="OSWP Student")
        osee_S_Role = discord.utils.get(server.roles, name="OSEE Student")
        oscp_V_Role = discord.utils.get(server.roles, name="OSCP Certified")
        oswe_V_Role = discord.utils.get(server.roles, name="OSWE Certified")
        osce_V_Role = discord.utils.get(server.roles, name="OSCE Certified")
        oswp_V_Role = discord.utils.get(server.roles, name="OSWP Certified")
        osee_V_Role = discord.utils.get(server.roles, name="OSEE Certified")
        wapt_S_Role = discord.utils.get(server.roles, name="WAPT Student")

        embed=discord.Embed(title="Student Statistics", description="Displays statistics about total members in the server, how many are in each student role, and how many are certified.", color=0x00ff00)
        embed.add_field(name="Total Members", value=totalMembers, inline=False)
        embed.add_field(name=oscp_S_Role, value=len(oscp_S_Role.members), inline=True)
        embed.add_field(name=oscp_V_Role, value=len(oscp_V_Role.members), inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=oswp_S_Role, value=len(oswp_S_Role.members), inline=True)
        embed.add_field(name=oswp_V_Role, value=len(oswp_V_Role.members), inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=oswe_S_Role, value=len(oswe_S_Role.members), inline=True)
        embed.add_field(name=oswe_V_Role, value=len(oswe_V_Role.members), inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=osce_S_Role, value=len(osce_S_Role.members), inline=True)
        embed.add_field(name=osce_V_Role, value=len(osce_V_Role.members), inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=osee_S_Role, value=len(osee_S_Role.members), inline=True)
        embed.add_field(name=osee_V_Role, value=len(osee_V_Role.members), inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name=wapt_S_Role, value=len(wapt_S_Role.members), inline=True)
        await channel.send(embed=embed)     

def setup(bot):
    bot.add_command(stats)

def teardown(bot):
    bot.remove_command(stats)
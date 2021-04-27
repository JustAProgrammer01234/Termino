import discord
from discord.ext import commands

@commands.command()
@commands.has_permissions(kick_members = True, administrator = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.send(f'Kicking: {member.mention}.')
    if reason is None:
        await member.kick(reason = "Didn't provide a reason.")
    else:
        await member.kick(reason = reason)

@commands.command()
@commands.has_permissions(ban_members = True, administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.send(f'Banning: {member.mention}')
    if reason is None:
        await member.ban(reason = "Didn't provide a reason.")
    else:
        await member.ban(reason = reason)

def add_command(bot):
    bot.add_command(kick)
    bot.add_command(ban)

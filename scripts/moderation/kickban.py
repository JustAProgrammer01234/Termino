import discord
from discord.errors import *
from discord.ext import commands

@commands.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    if reason is None:
        await member.kick(reason = "Didn't provide a reason.")
    else:
        await member.kick(reason = reason)

@commands.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    if reason is None:
        await member.ban(reason = "Didn't provide a reason.")
    else:
        await member.ban(reason = reason)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, Forbidden):
        await ctx.reply("Error: The bot doesn't have permissions to kick.")
    elif isinstance(error, MissingPermissions):
        await ctx.reply("Error: Permission denied.")

@kick.error
async def ban_error(ctx,error):
    if isinstance(error, Forbidden):
        await ctx.reply("Error: The bot doesn't have permissions to ban.")
    elif isinstance(error, MissingPermissions):
        await ctx.reply("Error: Permission denied.")

def add_command(bot):
    bot.add_command(kick)
    bot.add_command(ban)

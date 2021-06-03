import discord
import asyncio
from discord.ext import commands

@commands.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    embd = discord.Embed(title = f'Kicking {member.name}', color = discord.Colour.gold())
    send_embed_message = asyncio.create_task(ctx.send(embed = embd))
    if reason is None:
        kick_member = asyncio.create_task(member.kick(reason = "Didn't provide a reason."))
        await send_embed_message
        await kick_member
    else:
        kick_member = asyncio.create_task(member.kick(reason = "Didn't provide a reason."))
        await send_embed_message
        await kick_member

@commands.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    embd = discord.Embed(title = f'Banning {member.name}', color = discord.Colour.red())
    send_embed_message = asyncio.create_task(ctx.send(embed = embd))
    if reason is None:
        ban_member = asyncio.create_task(member.ban(reason = "Didn't provide a reason."))
        await member.ban(reason = "Didn't provide a reason.")
        await send_embed_message
        await ban_member

    else:
        ban_member = asyncio.create_task(member.ban(reason = reason))
        await send_embed_message
        await ban_member

#Commented this out because it's not working yet.
# @commands.command()
# @commands.has_permissions(ban_members = True)
# async def unban(ctx, *, member):
#     bans = await ctx.guild.bans()
#     user, discriminator = member.split('#')
#     for ban in bans:
#         banned_user = ban.user
#         if f'{banned_user.name}#{banned_user.discriminator}' == user + '#' + discriminator:
#             await ctx.guild.unban(member)
#             unbanned_member = f'{banned_user.name}#{banned_user.discriminator}'
#     unban_embed = discord.Embed(title = f'Unbanned {unbanned_member}')
#     await ctx.send(embed = unban_embed)

def add_command(bot):
    bot.add_command(kick)
    bot.add_command(ban)
    bot.add_command(unban)

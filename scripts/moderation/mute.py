import discord
import asyncio
from discord.ext import commands
from noncoroutines.funcs import *

@commands.command()
@commands.has_permissions(manage_roles = True)
async def add_mute_role(ctx, mute_role: discord.Role):
    data = get_server_data('data.json')
    if str(ctx.guild.id) in data:
        data[str(ctx.guild.id)]['mute_role'] = mute_role.id
        change_server_data('data.json',data)
        await ctx.reply('Mute role has now been added, now you can mute someone using the $mute command.')
    else:
        await ctx.reply(f'Bot not initialized yet, type $initialize.')

@commands.command()
@commands.has_permissions(manage_roles = True)
async def mute(ctx, member: discord.Member):
    data = get_server_data('data.json')
    embd = discord.Embed(title = f'Muting {member.name}', color = discord.Colour.purple())
    send_embed_message = asyncio.create_task(ctx.send(embed = embd))
    if str(ctx.guild.id) in data:
        mute_role = data[str(ctx.guild.id)]['mute_role']
        add_mute_role = asyncio.create_task(member.add_roles(member.guild.get_role(mute_role)))
        if mute_role != None:
            await send_embed_message
            await add_mute_role
        else:
            await ctx.reply("The bot doesn't know which mute role to add, have you tried the $add_mute_role command?")
    else:
        await ctx.reply(f'Bot not initialized yet, type $initialize.')

@commands.command()
@commands.has_permissions(manage_roles = True)
async def unmute(ctx, member: discord.Member):
    data = get_server_data('data.json')
    embd = discord.Embed(title = f'Unmuting {member.name}', color = discord.Colour.orange())
    send_embed_message = asyncio.create_task(ctx.send(embed = embd))
    if str(ctx.guild.id) in data:
        mute_role = data[str(ctx.guild.id)]['mute_role']
        remove_mute_role = asyncio.create_task(member.remove_roles(member.guild.get_role(mute_role)))
        if member.guild.get_role(mute_role) in member.roles:
            await send_embed_message
            await remove_mute_role
        else:
            await ctx.reply('Member is not muted.')
    else:
        await ctx.reply(f'Bot not initialized yet, type $initialize.')

def add_command(bot):
    bot.add_command(add_mute_role)
    bot.add_command(mute)
    bot.add_command(unmute)

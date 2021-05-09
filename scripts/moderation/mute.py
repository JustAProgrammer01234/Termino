import discord
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
    if str(ctx.guild.id) in data:
        mute_role = data[str(ctx.guild.id)]['mute_role']
        if mute_role != None:
            await member.add_roles(member.guild.get_role(mute_role))
        else:
            await ctx.reply("The bot doesn't know which mute role to add, have you tried the $add_mute_role command?")
    else:
        await ctx.reply(f'Bot not initialized yet, type $initialize.')

@commands.command()
@commands.has_permissions(manage_roles = True)
async def unmute(ctx, member: discord.Member):
    data = get_server_data('data.json')
    if str(ctx.guild.id) in data:
        mute_role = member.guild.get_role(data[str(ctx.guild.id)]['mute_role'])
        if mute_role in member.roles:
            await member.remove_roles(member.guild.get_role(mute_role.id))
        else:
            await ctx.reply('Member is not muted.')
    else:
        await ctx.reply(f'Bot not initialized yet, type $initialize.')

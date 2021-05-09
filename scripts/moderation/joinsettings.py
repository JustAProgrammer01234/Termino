import discord
from discord.ext import commands
from noncoroutines.funcs import *

@commands.command()
@commands.has_permissions(manage_roles = True)
async def set_channel_join(ctx, channel: discord.TextChannel):
    get_data = get_server_data('data.json')
    try:
        if str(ctx.guild.id) in get_data:
            get_data[str(ctx.guild.id)]['join_announcement_channel'] = channel.id
            change_server_data('data.json', get_data)
            await ctx.reply(f'Bot will send messages at {channel.mention} whenever a new member joins the server.')
        else:
            await ctx.reply(f'Bot not initialized yet, type $initialize.')
    except KeyError:
        await ctx.reply(f'Bot not initialized yet, type $initialize')

@commands.command()
@commands.has_permissions(manage_roles = True)
async def set_join_role(ctx, role: discord.Role):
    get_data = get_server_data('data.json')
    try:
        if str(ctx.guild.id) in get_data:
            if role in ctx.guild.roles:
                get_data[str(ctx.guild.id)]['join_role'] = role.id
                change_server_data('data.json', get_data)
                await ctx.reply(f'Bot will now add {role} to any user who joins the server.')
            else:
                await ctx.reply(f'Error: {role} does not exist in this server.')
        else:
            await ctx.reply(f'Bot not initialized yet, type $initialize')
    except KeyError:
        await ctx.reply(f'Bot not initialized yet, type $initialize.')

@commands.command()
@commands.has_permissions(manage_roles = True)
async def delete_join_role(ctx):
    get_data = get_server_data('data.json')
    if str(ctx.guild.id) in get_data:
        if get_data[str(ctx.guild.id)]['join_role'] != None:
            get_data[str(ctx.guild.id)]['join_role'] = None
            change_server_data('data.json', get_data)
            await ctx.reply(f'Successfully deleted join role {role.name}')
        else:
            await ctx.reply('I do not have role to add when a member joins this server.')
    else:
        await ctx.reply(f'Bot not initialized yet, type $initialize.')

@commands.command()
@commands.has_permissions(manage_roles = True)
async def delete_join_channel(ctx):
    get_data = get_server_data('data.json')
    if str(ctx.guild.id) in get_data:
        if get_data[str(ctx.guild.id)]['join_announcement_channel'] != None:
            get_data[str(ctx.guild.id)]['join_announcement_channel'] = None
            change_server_data('data.json',get_data)
            await ctx.reply('Succesfully deleted join channel.')
        else:
            await ctx.reply('I do not have a channel to say anything when a member joins this server.')
    else:
        await ctx.reply(f'Bot not initialized yet, type $initialize.')

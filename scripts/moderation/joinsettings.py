import discord
from discord.ext import commands
from noncoroutines.funcs import *

@commands.command()
@commands.has_permissions(manage_roles = True)
async def set_channel_join(ctx, channel: discord.TextChannel):
    try:
        get_data = get_server_data('data.json')
        get_data[str(ctx.guild.id)]['join_announcement_channel'] = channel.id
        change_server_data('data.json', get_data)
        await ctx.reply(f'Bot will send messages at {channel.mention} whenever a new member joins the server.')
    except KeyError:
        await ctx.reply(f'Bot not initialized yet, type out $initialize')

@commands.command()
@commands.has_permissions(manage_roles = True)
async def set_join_role(ctx, role: discord.Role):
    try:
        if role in ctx.guild.roles:
            get_data = get_server_data('data.json')
            get_data[str(ctx.guild.id)]['join_role'] = role.id
            change_server_data('data.json', get_data)
            await ctx.reply(f'Bot will now add {role} to any user who joins the server.')
        else:
            await ctx.reply(f'Error: {role} does not exist in this server.')
    except KeyError:
        await ctx.reply(f'Bot not initialized yet, type out $initialize')

import discord
from discord.ext import commands
from noncoroutines.funcs import *

@commands.command()
async def set_channel_join(ctx, channel: discord.TextChannel):
    get_data = get_server_data('data.json')
    get_data[ctx.guild.id]['join_announcement_channel'] = channel
    change_server_data('data.json', get_data)
    await ctx.reply(f'Bot will send messages at {channel.mention} whenever a new member joins the server.')

@commands.command()
async def set_join_role(ctx, channel: discord.TextChannel, role: discord.Role):
    if role in ctx.guild.roles:
        get_data = get_server_data('data.json')
        get_data[ctx.guild.id]['join_role'] = role
        change_server_data('data.json', get_data)
        await ctx.reply(f'Bot will now add {role} to any user who joins the server.')
    else:
        await ctx.reply(f'Error: {role} does not exist in this server.')

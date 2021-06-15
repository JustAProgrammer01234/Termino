import discord
import asyncio
from discord.ext import commands
from noncoroutines import get_server_data

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mp_mute = discord.Embed(title = ':no_entry: Permission denied! :no_entry:', description = 'You are missing the `Manage Roles` permission!', color = discord.Colour.red())

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member):
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
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: discord.Member):
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

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_mute)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_mute)

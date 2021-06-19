import discord
import asyncio
from discord.ext import commands

class KickBan(commands.Cog):
    '''
    Commands related to kicking and banning members from guild.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.mp_kick = discord.Embed(title = ':no_entry: Permission denied! :no_entry:', description = 'You are missing the `Kick Members` permission.', color = discord.Colour.red())
        self.mp_ban = discord.Embed(title = ':no_entry: Permission denied! :no_entry:', description = 'You are missing the `Ban Members` permission.', color = discord.Colour.red())

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
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
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
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

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        ban_list = await ctx.guild.bans()
        name, discriminator = member.split('#')
        message = await ctx.send('Hold on this may take a while.')
        unban_embed = discord.Embed(title = f'{name}#{discriminator} has been unbanned.', color = discord.Colour.green())
        found_member = False

        for ban_entry in ban_list:
            user = ban_entry.user
            if f'{name}#{discriminator}' == f'{user.name}#{user.discriminator}':
                await ctx.guild.unban(user)
                await message.delete()
                await ctx.send(f'{name}#{discriminator} has been unbanned.')
                found_member = True
                break

        if not found_member:
            await message.delete()
            await ctx.send("Couldn't find banned member.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def banlist(self, ctx):
        ban_list = await ctx.guild.bans()
        bans_label = ''
        message = await ctx.send('Hold on this may take a while.')
        for ban_entry in ban_list:
            user = ban_entry.user
            bans_label += f'{user.name}#{user.discriminator}\n'
        banlist_embed = discord.Embed(title = f'Banned members in {ctx.guild}:',
            description = f'```{bans_label}```',
            color = discord.Colour.red())
        await message.delete()
        if bans_label == '':
            await ctx.send('Looks like I found no banned members.')
        else:
            await ctx.send(embed = banlist_embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_kick)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_ban)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_ban)

    @banlist.error 
    async def banlist_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_ban)
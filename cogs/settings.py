import discord 
from discord.ext import commands 
from .util.database.termino_servers import TerminoServers

class Settings(commands.Cog, name = 'settings'):
    '''
    This category contains all of the config commands.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.servers_db = self.bot.servers_db

    def __str__(self):
        return ':gear: Settings :gear:'

    @commands.Cog.listener()
    async def on_member_join(self, member):
        server_info = await self.servers_db.fetch_server_info(member.guild.id)

        welcome_channel = server_info['welcome_channel_id']
        welcome_role = server_info['welcome_role_id']
        welcome_dm = server_info['welcome_dm']

        welcome_embed = discord.Embed(title = 'Someone joined the server!', description = f'''
        ***Welcome {member}!***
        > **Users: `{len([m for m in member.guild.members if not m.bot])}`**
        > **Bots: `{len([m for m in member.guild.members if m.bot])}`**
        > Total: **`{member.guild.member_count}`**
        ''', color = discord.Colour.from_rgb(255,255,255))
        welcome_embed.set_image(url = member.avatar_url)

        if welcome_channel is not None:
            c = member.guild.get_channel(welcome_channel)
            await c.send(embed = welcome_embed)

        if welcome_channel is not None:
            r = member.guild.get_role(welcome_role)
            await member.add_roles(r)

        if welcome_dm is not None:
            await member.send(welcome_dm)

    @commands.command(name = 'set-welcome-channel')
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def set_welcome_channel(self, ctx, channel: commands.TextChannelConverter):
        '''
        Tells the bot to send welcome messages to users who joins the server in a specific channel.
        '''
        await self.servers_db.update_welcome_channel(ctx.guild.id, channel.id)
        await ctx.send(f':white_check_mark: ***Successfully set welcome channel to {channel.mention}*** :white_check_mark:')

    @commands.command(name = 'set-welcome-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def set_welcome_role(self, ctx, role: commands.RoleConverter):
        '''
        Tells the bot to add a role to users who join the server.
        '''
        await self.servers_db.update_welcome_role(ctx.guild.id, role.id)
        await ctx.send(f':white_check_mark: ***Sucessfully set welcome role to {role}.*** :white_check_mark:')

    @commands.command(name = 'welcome-dm-message')
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def welcome_dm_message(self, ctx, *, message):
        '''
        Tells the bot to dm users who join the server.
        '''
        await self.servers_db.update_welcome_dm(ctx.guild.id, message)
        await ctx.send(':white_check_mark: ***Now the bot will send dms to users who join the server.*** :white_check_mark:')

    @commands.command(name = 'add-no-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def add_no_role(self, ctx):
        '''
        Tells the bot to stop adding roles to users who join the server.
        '''
        await self.servers_db.update_welcome_role(ctx.guild.id, None)
        await ctx.send(':white_check_mark: ***Now the bot will not assign roles to users who join the server.*** :white_check_mark:')

    @commands.command(name = 'no-welcome')
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def no_welcome(self, ctx):
        '''
        Tells the bot to stop sending welcome messages.
        '''
        await self.servers_db.update_welcome_channel(ctx.guild.id, None)
        await ctx.send(':white_check_mark: ***The bot will not send welcome messages when someone joins the server.*** :white_check_mark:')

    @commands.command(name = 'no-welcome-dm')
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def no_welcome_dm(self, ctx):
        '''
        Tells the bot to stop sending welcome dms.
        '''
        await self.servers_db.update_welcome_dm(ctx.guild.id, None)
        await ctx.send(':white_check_mark: ***The bot will not send dms to users who join the server.*** :white_check_mark:')

    @commands.command(name = 'select-mute-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def select_mute_role(self, ctx, mute_role: commands.RoleConverter):
        '''
        This command allows you to select an existing mute role. (This is for servers who already have a mute role included.)
        '''
        await self.servers_db.update_mute_role(ctx.guild.id, mute_role.id)
        await ctx.send(f':white_check_mark: ***Succesfully set mute role to {mute_role}.*** :white_check_mark:')

    @commands.command()
    async def set_prefix(self, ctx, prefix):
        '''
        Changes the bot's prefix for this server.
        '''
        await self.servers_db.update_prefix(ctx.guild.id, prefix)
        await ctx.send(f':white_check_mark: ***Succesfully updated prefix to {prefix}*** :white_check_mark:')

def setup(bot):
    bot.add_cog(Settings(bot))
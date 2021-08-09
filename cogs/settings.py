import discord 
from discord.ext import commands 

class Settings(commands.Cog, name = 'settings'):
    '''
    This category contains all of the config commands.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    @commands.command(name = 'set-welcome-channel')
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def set_welcome_channel(self, ctx, channel: discord.TextChannel):
        '''
        Tells the bot to send welcome messages to users who joins the server in `<channel>`
        '''
        pass

    @commands.command(name = 'set-join-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def set_join_role(self, ctx, role: commands.RoleConverter):
        '''
        Tells the bot to add `<role>` to users who joins the server.
        '''
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'welcome-dm-message')
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def welcome_dm_message(self, ctx, *, message):
        '''
        Tells the bot to dm users `<message>` who joins the server.
        '''
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'add-no-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def add_no_role(self, ctx):
        '''
        Tells the bot to stop adding roles to users who join the server.
        '''
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'no-welcome')
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def no_welcome(self, ctx):
        '''
        Tells the bot to stop sending welcome messages.
        '''
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'no-welcome-dm')
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def no_welcome_dm(self, ctx):
        '''
        Tells the bot to stop sending welcome dms.
        '''
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'select-mute-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def select_mute_role(self, ctx, mute_role: commands.RoleConverter):
        '''
        This command allows you to select an existing mute role. (This is for servers who already have a mute role included!)
        '''
        await ctx.send('This command is under maintenance.')


    # @set_join_channel.error
    # async def set_channel_join_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(embed = self.mp_manage_channels)
    
    # @set_join_role.error
    # async def set_join_role_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(embed = self.mp_manage_roles)

    # @welcome_dm_message.error
    # async def welcome_dm_message_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(embed = self.mp_manage_messages)

    # @remove_join_role.error
    # async def remove_join_role_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(embed = self.mp_manage_roles)

    # @remove_join_channel.error
    # async def remove_join_channel_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(embed = self.mp_manage_channels)

    # @remove_dm_message.error
    # async def remove_dm_message_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(embed = self.mp_manage_messages)

    # @add_mute_role.error 
    # async def add_mute_role_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(embed = self.mp_manage_roles)

    # @remove_mute_role.error 
    # async def add_mute_role_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(embed = self.mp_manage_roles)

def setup(bot):
    bot.add_cog(Settings(bot))
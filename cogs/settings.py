import discord 
from discord.ext import commands 

class Settings(commands.Cog, name = 'settings'):
    '''
    Commands related to welcome settings.
    '''
    def __init__(self, bot):
        self.bot = bot
        # self.server_data = get_json_data('data.json')
        # self.mp_manage_channels = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
        #     description = 'You are missing the `Manage Channels` permission.',
        #     color = discord.Colour.red()
        # )
        # self.mp_manage_messages = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
        #     description = 'You are missing the `Manage Messages` permission.',
        #     color = discord.Colour.red()
        # )
        # self.mp_manage_roles = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
        #     description = 'You are missing the `Manage Roles` permission.',
        #     color = discord.Colour.red()
        # )
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # join_announcement_channel = self.server_data[str(member.guild.id)]["join_announcement_channel"]
        # welcome_dm = self.server_data[str(member.guild.id)]["welcome_dm"]
        # join_role = self.server_data[str(member.guild.id)]["join_role"]
        # welcome_embed = welcome_embed = discord.Embed(
        #     title = f'Looks like someone joined the server!',
        #     description = f'Welcome {member.mention}!',
        #     color = discord.Colour.green())
        # welcome_embed.add_field(
        #     name = 'Number of members:',
        #     value = f'`Total: {len(member.guild.members)}`\n`Not including bots: {len([member for member in member.guild.members if not member.bot])}`')
        # welcome_embed.set_image(
        #     url = member.avatar_url
        # )

        # if join_announcement_channel != None:
        #     await self.bot.get_channel(join_announcement_channel).send(embed = welcome_embed)

        # if welcome_dm != None:
        #     await member.send(welcome_dm)

        # if join_role != None:
        #     await member.add_roles(member.guild.get_role(join_role))
        pass

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # if str(guild.id) not in self.server_data:
        #     self.server_data[str(guild.id)] = {"mute_role":None, "join_announcement_channel": None, "join_role": None, "welcome_dm": None}
        #     change_json_data('data.json', self.server_data)
        pass

    @commands.command(name = 'set-join-channel')
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def set_join_channel(self, ctx, channel: discord.TextChannel):
        '''
        __**Description:**__
        Tells the bot to send welcome messages to users who joins the server in `<channel>`

        __**Arguments:**__
        **1.** `<channel>` - The channel to send welcome messages in. (This argument must contain the channel's id or a channel mention and must be a text channel.)
        '''
        # self.server_data[str(ctx.guild.id)]['join_announcement_channel'] = channel.id
        # change_json_data('data.json', self.server_data)
        # await ctx.reply(f'Bot will send messages at {channel.mention} whenever a new member joins the server.')
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'set-join-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def set_join_role(self, ctx, role: commands.RoleConverter):
        '''
        __**Description:**__
        Tells the bot to add `<role>` to users who joins the server.

        __**Arguments:**__
        **1.** `<role>` - The role the bot will add. (It is not required that you ping the role for `<role>`,  but it is recommended that you put the role's id for the bot to know which specific role to add.)
        '''
        # if role in ctx.guild.roles:
        #     self.server_data[str(ctx.guild.id)]['join_role'] = role.id
        #     change_json_data('data.json', self.server_data)
        #     await ctx.reply(f'Bot will now add {role} to any user who joins the server.')
        # else:
        #     await ctx.reply(f'Error: {role} does not exist in this server.')
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'welcome-dm-message')
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def welcome_dm_message(self, ctx, *, message):
        '''
        __**Description:**__
        Tells the bot to dm users `<message>` who joins the server.

        __**Arguments:**__
        **1.** `<message>` - The message to dm.
        '''
        # self.server_data[str(ctx.guild.id)]['welcome_dm'] = message
        # change_json_data('data.json', self.server_data)
        # await ctx.reply('Bot will now dm this message when a member joins this server.')
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'add-no-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def add_no_role(self, ctx):
        '''
        __**Description:**__
        Tells the bot to stop adding roles to users who join the server.

        __**Arguments:**__
        No arguments are found in this command.
        '''
        # self.server_data[str(ctx.guild.id)]['join_role'] = None
        # change_json_data('data.json', self.server_data)
        # await ctx.reply('Join role deleted.')
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'no-welcome')
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def no_welcome(self, ctx):
        '''
        __**Description:**__
        Tells the bot to stop sending welcome messages.

        __**Arguments:**__
        No arguments are found in this command.
        '''
        # self.server_data[str(ctx.guild.id)]['join_announcement_channel'] = None
        # change_json_data('data.json', self.server_data)
        # await ctx.reply(f'Bot will stop sending welcome messages in server.')
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'no-welcome-dm')
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def no_welcome_dm(self, ctx):
        '''
        __**Description:**__
        Tells the bot to stop sending welcome dms.

        __**Arguments:**__
        No arguments are found in this command.
        '''
        # self.server_data[str(ctx.guild.id)]['welcome_dm'] = None
        # change_json_data('data.json', self.server_data)
        # await ctx.reply('Bot will stop sending direct messages to users who joins this server.')
        await ctx.send('This command is under maintenance.')

    @commands.command(name = 'select-mute-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def select_mute_role(self, ctx, mute_role: commands.RoleConverter):
        '''
        __**Description:**__
        This command allows you to select a mute role. (This is for servers who already have a mute role included!)

        __**Arguments:**__
        **1.** `<mute_role>` - The mute role to be selected. (It is not required that you ping the role for `<mute_role>`,  but it is recommended that you put the role's id for the bot to know which specific role to add.)
        '''
        # self.server_data[str(ctx.guild.id)]['mute_role'] = mute_role.id
        # change_json_data('data.json', self.server_data)
        # await ctx.send("Mute role has now been added.")
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
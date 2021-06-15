import discord
from discord.ext import commands
from noncoroutines import change_server_data, UtilClass

class JoinSettings(UtilClass, commands.Cog):
    def __init__(self, bot):
        super().__init__(bot)
        self.mp_manage_channels = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
            description = 'You are missing the `Manage Channels` permission.',
            color = discord.Colour.red()
        )
        self.mp_manage_messages = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
            description = 'You are missing the `Manage Messages` permission.',
            color = discord.Colour.red()
        )
        self.mp_manage_roles = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
            description = 'You are missing the `Manage Roles` permission.',
            color = discord.Colour.red()
        )

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join_announcement_channel = self.server_data[str(member.guild.id)]["join_announcement_channel"]
        welcome_dm = self.server_data[str(member.guild.id)]["welcome_dm"]
        join_role = self.server_data[str(member.guild.id)]["join_role"]
        welcome_embed = welcome_embed = discord.Embed(
            title = f'Looks like someone joined the server!',
            description = f'Welcome {member.mention}!',
            color = discord.Colour.green())
        welcome_embed.add_field(
            name = 'Number of members:',
            value = f'`Total: {len(member.guild.members)}`\n`Not including bots: {len([member for member in member.guild.members if not member.bot])}`')

        if join_announcement_channel != None:
            await self.bot.get_channel(join_announcement_channel).send(embed = welcome_embed)

        if welcome_dm != None:
            await member.send(welcome_dm)

        if join_role != None:
            await member.add_roles(self.bot.get_role(join_role))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if str(guild.id) not in self.server_data:
            self.server_data[str(guild.id)] = {"mute_role":None, "join_announcement_channel": None, "join_role": None, "welcome_dm": None}
            change_server_data('data.json', self.server_data)

    @commands.command(name = 'set-channel-join')
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def set_channel_join(self, ctx, channel: discord.TextChannel):
        self.server_data[str(ctx.guild.id)]['join_announcement_channel'] = channel.id
        change_server_data('data.json', self.server_data)
        await ctx.reply(f'Bot will send messages at {channel.mention} whenever a new member joins the server.')

    @commands.command(name = 'set-join-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def set_join_role(self, ctx, role: commands.RoleConverter):
        if role in ctx.guild.roles:
            self.server_data[str(ctx.guild.id)]['join_role'] = role.id
            change_server_data('data.json', self.server_data)
            await ctx.reply(f'Bot will now add {role} to any user who joins the server.')
        else:
            await ctx.reply(f'Error: {role} does not exist in this server.')

    @commands.command(name = 'welcome-dm-message')
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def welcome_dm_message(self, ctx, message):
        self.server_data[str(ctx.guild.id)]['welcome_dm'] = message
        change_server_data('data.json', self.server_data)
        await ctx.reply('Bot will now dm this message when a member joins this server.')

    @commands.command(name = 'remove-join-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def remove_join_role(self, ctx):
        self.server_data[str(ctx.guild.id)]['join_role'] = None
        change_server_data('data.json', self.server_data)
        await ctx.reply('Join role deleted.')

    @commands.command(name = 'remove-join-channel')
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def remove_join_channel(self, ctx):
        self.server_data[str(ctx.guild.id)]['join_announcement_channel'] = None
        change_server_data('data.json', self.server_data)
        await ctx.reply(f'Bot will stop sending welcome messages in server.')

    @commands.command(name = 'remove-dm-message')
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def remove_dm_message(self, ctx):
        self.server_data[str(ctx.guild.id)]['welcome_dm'] = None
        change_server_data('data.json', self.server_data)
        await ctx.reply('Bot will stop sending direct messages to users who joins this server.')

    @set_channel_join.error
    async def set_channel_join_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_manage_channels)
    
    @set_join_role.error
    async def set_join_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_manage_roles)

    @welcome_dm_message.error
    async def welcome_dm_message_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_manage_messages)

    @remove_join_role.error
    async def remove_join_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_manage_roles)

    @remove_join_channel.error
    async def remove_join_channel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_manage_channels)

    @remove_dm_message.error
    async def remove_dm_message_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_manage_messages)
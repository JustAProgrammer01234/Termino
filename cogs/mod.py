import discord 
import asyncio
from discord.ext import commands

kick_gif = 'https://media1.tenor.com/images/e4e4730bdc422c5f75b1126926077485/tenor.gif?itemid=4799973'
ban_gif = 'https://media.tenor.com/images/76f50d3ec6888dd3552db1d074435022/tenor.gif'
mute_gif = 'https://media1.tenor.com/images/b54c8e343c06dc160c4fc270f8ff0ae8/tenor.gif?itemid=17545855'

class DurationConverter(commands.Converter):
    async def convert(self, ctx, duration):
        time_unit_value = {'s': 1, 'm': 60, 'h': 120}
        num, time_unit = int(duration[:-1]), time_unit_value[duration[-1]]

        if time_unit in time_unit_value.values():
            return num * time_unit

class Mod(commands.Cog, name = 'mod'):
    '''
    This command category contains all the moderator commands.
    '''
    def __init__(self, bot):
        self.bot = bot 
        self.mp_user = discord.Embed(title = ':no_entry: Permission denied! :no_entry:', color = discord.Colour.red())
        self.mp_user.description = 'Or you may be affected by hierarchy.'
        self.mp_bot = discord.Embed(title = ':warning: Bot has missing perms! :warning:', color = discord.Colour.red())
        self.mp_bot.description = 'Or the bot may be affected by hierarchy.'

    def __repr__(self):
        return ':shield: Moderation :shield:'

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_user)
        elif isinstance(error, commands.CommandInvokeError):
            if hasattr(error, 'original'):
                if isinstance(error.original, discord.Forbidden):
                    await ctx.send(embed = self.mp_bot)

    @commands.group()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def role(self, ctx):
        '''
        Command group that contains sub commands for creating roles in a server.

        You must have Manage Roles Perm to do this. The same goes for the bot.
        '''
        await ctx.send_help('role')

    @role.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def create(self, ctx, role_name, *, reason = None):
        '''
        Creates a role.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        if reason is None:
            await ctx.guild.create_role(name = role_name, reason = f'Role created by: {ctx.author}')
        else:
            await ctx.guild.create_role(name = role_name, reason = reason)
        
        await ctx.send('Role successfully created.')

    @role.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def add(self, ctx, role: commands.RoleConverter, member: commands.MemberConverter, reason = None):
        '''
        Adds a role to a member.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        if reason is None:
            await member.add_role(role = role, reason = f'Role added by: {ctx.author}')
        else:
            await member.add_role(role = role, reason = reason)

        await ctx.send(f'Sucessfully added role to **{member}**.')

    @commands.group(name = 'create-channel', invoke_without_command = True)
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def create_channel(self, ctx):
        '''
        Command group that contains sub commands for creating channels in a server.

        You must have Manage Channels perm to do this. The same goes for the bot.
        '''
        await ctx.send_help('create-channel')

    @create_channel.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def text(self, ctx, channel_name, *, reason = None):
        '''
        Creates a text channel.

        You must have Manage Channels perm to do this. The same goes for the bot.
        '''
        if reason is None:
            await ctx.guild.create_text_channel(name = channel_name, reason = f'Text channel created by: {ctx.author}')
        else:
            await ctx.guild.create_text_channel(name = channel_name, reason = reason)

        await ctx.send('Text channel sucesssfully created.')

    @create_channel.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def voice(self, ctx, channel_name, reason = None):
        '''
        Creates a voice channel.

        You must have Manage Channels perm to do this. The same goes for the bot.
        '''
        if reason is None:
            await ctx.guild.create_voice_channel(name = channel_name, reason = f'Voice channel created by: {ctx.author}')
        else:
            await ctx.guild.create_voice_channel(name = channel_name, reason = reason)
            
        await ctx.send('Voice channel successfully created.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, limit: int):
        '''
        Purges or deletes the number of messages or `limit` in the channel the command is called. 

        You must have Manage Messages perm to do this. The same goes for the bot.
        '''
        await ctx.channel.purge(limit = limit)
        await ctx.send(f'Successfully deleted {limit} messages.')
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason = None):
        '''
        Kicks a member.

        You must have Kick Members perm to do this. The same goes for the bot.
        '''
        embd = discord.Embed(title = f':mechanical_leg: ***Kicked {member.name}#{member.discriminator}*** :mechanical_leg:', color = discord.Colour.from_rgb(255,255,255))
        embd.set_thumbnail(url = kick_gif)
    
        if reason is None:
            embd.add_field(name = 'Reason for kick:', value = f"Kicked by: {ctx.author}")
            await member.kick(reason = "Didn't provide a reason.")
            await ctx.send(embed = embd)
        else:
            embd.add_field(name = 'Reason for kick:', value = reason)
            await member.kick(reason = reason)
            await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason = None):
        '''
        Bans a member.

        You must have Ban Members perm to do this. The same goes for the bot.
        '''
        embd = discord.Embed(title = f':hammer: ***Banned {member.name}#{member.discriminator}*** :hammer:', color = discord.Colour.from_rgb(255,255,255))
        embd.set_thumbnail(url = ban_gif)

        if reason is None:
            embd.add_field(name = 'Reason for ban:', value = f"Banned by: {ctx.author}")
            await member.ban(reason = "Didn't provide a reason.")
            await ctx.send(embed = embd)
        else:
            embd.add_field(name = 'Reason for ban:', value = reason)
            await member.ban(reason = reason)
            await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter, *, reason = None):
        '''
        Temporarily bans a member.

        You must have Ban Members perm to do this. The same goes for the bot.
        '''
        embd = discord.Embed(title = f':hammer: ***Temporarily banned {member.name}#{member.discriminator}*** :hammer:', color = discord.Colour.from_rgb(255,255,255))
        embd.set_thumbnail(url = ban_gif)

        if reason is None:
            embd.add_field(name = 'Reason for ban:', value = f"Temporarily banned by: {ctx.author}")
            await member.ban(reason = "Didn't provide a reason.")
            await ctx.send(embed = embd)
        else:
            embd.add_field(name = 'Reason for ban:', value = reason)
            await member.ban(reason = reason)
            await ctx.send(embed = embd)
  
        await asyncio.sleep(duration)
        await member.unban(reason = 'Temporary ban already ended.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        '''
        Unbans a member

        You must have Ban Members perm to do this. The same goes for the bot.
        '''
        ban_list = await ctx.guild.bans()
        name, discriminator = member.split('#')
        message = await ctx.send('Hold on this may take a while.')
        found_member = False

        for ban_entry in ban_list:
            user = ban_entry.user
            if f'{name}#{discriminator}' == f'{user.name}#{user.discriminator}':
                await ctx.guild.unban(user, reason = f'Unbanned by: {ctx.author}')
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
        '''
        Sends a list of banned members.

        You must have Ban Members perm to do this. The same goes for the bot.
        '''
        bans_label = ''
        ban_list = await ctx.guild.bans()
        banlist_embed = discord.Embed(title = f'Banned users in {ctx.guild}:', color = discord.Colour.from_rgb(255,255,255))
        greater_than_one = len(ban_list) > 1

        if len(ban_list) > 0:
            if greater_than_one:
                message = await ctx.send(f'I found **{len(ban_list)}** users banned, listing them one by one.')

            for ban_entry in ban_list:
                user = ban_entry.user
                bans_label += f'{user.name}#{user.discriminator}\n'

            if greater_than_one:
                await message.delete()
                
            banlist_embed.description = f'```{bans_label}```'
            await ctx.send(embed = banlist_embed)
        else:
            await ctx.send("This server has no banned members.")
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: commands.MemberConverter, duration: DurationConverter = None, reason = None):
        '''
        Mutes a member in both text and voice channels.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        await ctx.send('This command is under maintenance.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: commands.MemberConverter):
        '''
        Unmutes a member in both text and voice channels.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        await ctx.send('This command is under maintenance.')

def setup(bot):
    bot.add_cog(Mod(bot))
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

    def __str__(self):
        return ':shield: Mod :shield:'

    @commands.command(name = 'add-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def add_role(self, ctx, role: commands.RoleConverter, member: commands.MemberConverter, reason = None):
        '''
        Adds a role to a member.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        if reason is None:
            await member.add_roles(role, reason = f'No reason provided.')
        else:
            await member.add_roles(role, reason = reason)

        await ctx.send(f'Sucessfully added role to **{member}**.')            

    @commands.command(name = 'remove-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def remove_role(self, ctx, role: commands.RoleConverter, member: commands.MemberConverter, reason = None):
        '''
        Removes a role from a member.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        if reason is None:
            await member.remove_roles(role, reason = f'No reason provided.')
        else:
            await member.remove_roles(role, reason = reason)

        await ctx.send(f'Sucessfully removed role from **{member}**.')   

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, limit: int):
        '''
        Purges or deletes the number of messages or `limit` in the channel the command is called. 

        You must have Manage Messages perm to do this. The same goes for the bot.
        '''
        await ctx.channel.purge(limit = limit)
        await ctx.author.send(f'**Successfully deleted `{limit}` messages.**')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def lock(self, ctx, channel: commands.TextChannelConverter):
        '''
        Locks a channel.   

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        await channel.set_permissions(ctx.guild.default_role, send_messages = False)
        await ctx.send(f'**Successfully locked {channel.mention}.**')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unlock(self, ctx, channel: commands.TextChannelConverter):
        '''
        Unlocks a channel.

        You must have Manage Messages perm to do this. The same goes for the bot.
        '''
        await channel.set_permissions(ctx.guild.default_role, send_messages = True)
        await ctx.send(f'**Successfully unlocked {channel.mention}.**')
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason = None):
        '''
        Kicks a member.

        You must have Kick Members perm to do this. The same goes for the bot.
        '''
        embd = discord.Embed(title = f':mechanical_leg: ***Kicked {member}*** :mechanical_leg:', color = discord.Colour.from_rgb(255,255,255))
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
        embd = discord.Embed(title = f':hammer: ***Banned {member}*** :hammer:', color = discord.Colour.from_rgb(255,255,255))
        embd.set_thumbnail(url = ban_gif)

        if reason is None:
            embd.add_field(name = 'Reason for ban:', value = f'No reason provided.')
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
        embd = discord.Embed(title = f':hammer: ***Temporarily banned {member}*** :hammer:', color = discord.Colour.from_rgb(255,255,255))
        embd.set_thumbnail(url = ban_gif)

        if reason is None:
            embd.add_field(name = 'Reason for ban:', value = f'No reason provided.')
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
        async with ctx.typing():
            found_member = False

            async for ban_entry in ctx.guild.bans():
                user = ban_entry.user
                if f'{member}' == f'{user}':
                    await ctx.guild.unban(user, reason = f'Unbanned by: {ctx.author}')
                    await ctx.send(f'{member} has been unbanned.')
                    found_member = True
                    break

            if not found_member:
                await ctx.send("Couldn't find banned member.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def banlist(self, ctx):
        '''
        Sends a list of banned members.

        You must have Ban Members perm to do this. The same goes for the bot.
        '''
        ban_list = await ctx.guild.bans()
        banlist_embed = discord.Embed(
            title = f'{len(ban_list)} banned users in {ctx.guild}:', 
            color = discord.Colour.from_rgb(255,255,255)
        )
        async with ctx.typing():
            if len(ban_list) > 0:
                for ban_entry in ban_list:
                    banlist_embed.add_field(name = str(ban_entry[1]), value = f'__Reason:__\n`{ban_entry[0]}`', inline = False)
                await ctx.send(embed = banlist_embed)
            else:
                await ctx.send("This server has no banned members.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: commands.MemberConverter, reason = None):
        '''
        Mutes a member in both text and voice channels.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        await ctx.send('This command is under maintenance.')
    
    @commands.command(name = 'temp-mute')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def temp_mute(self, ctx, member: commands.MemberConverter, duration: DurationConverter = None, reason = None):
        '''
        Temporarily mutes a member in both text and voice channels.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        await ctx.send('This command is under maintenance.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: commands.MemberConverter, reason = None):
        '''
        Unmutes a member in both text and voice channels.

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        await ctx.send('This command is under maintenance.')

def setup(bot):
    bot.add_cog(Mod(bot))
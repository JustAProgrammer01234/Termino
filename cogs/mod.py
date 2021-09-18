import re 
import discord 
import asyncio
from discord.ext import commands

time_re = re.compile(r"(\d{1,5}(?:[.,]?\d{1,5})?)([smhd])")
time_dict = {"s":1, "m":60, "h":3600, "d":86400}

kick_gif = 'https://media1.tenor.com/images/e4e4730bdc422c5f75b1126926077485/tenor.gif?itemid=4799973'
ban_gif = 'https://media.tenor.com/images/76f50d3ec6888dd3552db1d074435022/tenor.gif'
mute_gif = 'https://media1.tenor.com/images/b54c8e343c06dc160c4fc270f8ff0ae8/tenor.gif?itemid=17545855'

class DurationConverter(commands.Converter):
    async def convert(self, ctx, duration):
        matches = time_re.findall(duration)
        time = 0 
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                raise commands.BadArgument(f"{k} is an invalid time-key! h/m/s/d are valid!")
            except ValueError:
                raise commands.BadArgument(f"{v} is not a number!")
        return time

class Mod(commands.Cog):
    '''
    This category contains all the moderator commands.
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

        await ctx.send(rf'\:white_check_mark: Sucessfully added role to **{member}**.')            

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

        await ctx.send(rf'\:white_check_mark: Sucessfully removed role from **{member}**.')   

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, limit: int):
        '''
        Purges or deletes the number of messages or `limit` in the channel the command is called. 

        You must have Manage Messages perm to do this. The same goes for the bot.
        '''
        await ctx.channel.purge(limit = limit)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def lock(self, ctx, channel: commands.TextChannelConverter):
        '''
        Locks a channel.   

        You must have Manage Roles perm to do this. The same goes for the bot.
        '''
        await ctx.message.add_reaction('\U0001f512')
        await channel.set_permissions(ctx.guild.default_role, send_messages = False)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unlock(self, ctx, channel: commands.TextChannelConverter):
        '''
        Unlocks a channel.

        You must have Manage Messages perm to do this. The same goes for the bot.
        '''
        await ctx.message.add_reaction('\U0001f513')
        await channel.set_permissions(ctx.guild.default_role, send_messages = True)
    
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
        else:
            embd.add_field(name = 'Reason for ban:', value = reason)
            await member.ban(reason = reason)
            
        await ctx.send(embed = embd)
        await asyncio.sleep(duration)
        await member.unban(reason = 'Temporary ban already ended.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, member_id: int, reason = None):
        '''
        Unbans a member using the member id.

        You must have Ban Members perm to do this. The same goes for the bot.
        '''
        banned_member = discord.Object(id = member_id)

        if reason is None:
            reason = 'No reason provided.'
        else:
            reason = reason 

        try:
            await ctx.guild.unban(banned_member, reason = reason)
        except discord.NotFound:
            await ctx.send("Couldn't find that banned member.")
        else:
            await ctx.send(rf"\:white_check_mark: Successfully unbanned **{banned_member}**.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def banlist(self, ctx):
        '''
        Sends a list of banned members.

        You must have Ban Members perm to do this. The same goes for the bot.
        '''
        ban_list = await ctx.guild.bans()
        banlist_embed = discord.Embed(title = f'{len(ban_list)} banned users in {ctx.guild}:')

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
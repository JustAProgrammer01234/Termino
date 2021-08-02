import discord 
import asyncio
from .util import converters
from discord.ext import commands

class Mod(commands.Cog, name = 'mod'):
    '''
    This command category contains all the moderator commands.
    '''
    def __init__(self, bot):
        self.bot = bot 
        self.kick_gif = 'https://media1.tenor.com/images/e4e4730bdc422c5f75b1126926077485/tenor.gif?itemid=4799973'
        self.ban_gif = 'https://media.tenor.com/images/76f50d3ec6888dd3552db1d074435022/tenor.gif'
        self.mute_gif = 'https://media1.tenor.com/images/b54c8e343c06dc160c4fc270f8ff0ae8/tenor.gif?itemid=17545855'
        self.mp_user = discord.Embed(title = ':no_entry: Permission denied! :no_entry:', color = discord.Colour.red())
        self.mp_bot = discord.Embed(title = ':warning: Bot has missing perms! :warning:', color = discord.Colour.red())
        self.mp_bot.set_footer(text = 'Or it may be affected by hierarchy.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason = None):
        '''
        Kicks a member.
        '''
        embd = discord.Embed(title = f':mechanical_leg: Kicked {member.name}#{member.discriminator} :mechanical_leg:', color = discord.Colour.green())
        embd.set_thumbnail(url = self.kick_gif)
        if reason is None:
            embd.add_field(name = 'Reason for kick:', value = "Didn't provide a reason.")
            await member.kick(reason = "Didn't provide a reason.")
            await ctx.send(embed = embd)
        else:
            embd.add_field(name = 'Reason for kick:', value = reason)
            await member.kick(reason = reason)
            await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason = None, duration: converters.DurationConverter = None):
        '''
        Bans a member.
        '''
        member_id = member.id
        embd = discord.Embed(title = f':hammer: Banned {member.name}#{member.discriminator} :hammer:', color = discord.Colour.green())
        embd.set_thumbnail(url = self.ban_gif)

        if reason == None:
            embd.add_field(name = 'Reason for ban:', value = "Didn't provide a reason.")
            await member.ban(reason = "Didn't provide a reason.")
            await ctx.send(embed = embd)
        else:
            embd.add_field(name = 'Reason for ban:', value = reason)
            await member.ban(reason = reason)
            await ctx.send(embed = embd)

        if duration != None:
            await asyncio.sleep(duration)
            await ctx.guild.unban(member_id, reason = 'Temporary ban already ended.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        '''
        Unbans a member
        '''
        ban_list = await ctx.guild.bans()
        name, discriminator = member.split('#')
        message = await ctx.send('Hold on this may take a while.')
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
        '''
        Sends a list of banned members.
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
    async def mute(self, ctx, member: commands.MemberConverter, duration: converters.DurationConverter = None, reason = None):
        '''
        Mutes a member in both text and voice channels.
        '''
        await ctx.send('This command is under maintenance.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: commands.MemberConverter):
        '''
        Unmutes a member in both text and voice channels.
        '''
        await ctx.send('This command is under maintenance.')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            self.mp_user.description = "You are missing the `Kick Members` permission!"
            await ctx.send(embed = self.mp_user)
        elif hasattr(error, 'original'):
            if isinstance(error.original, discord.Forbidden):
                self.mp_bot.description = "The bot is missing the `Kick Members` permission!" 
                await ctx.send(embed = self.mp_bot)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Ban Members` permission!"
            await ctx.send(embed = self.mp_user)
        elif hasattr(error, 'original'):
            if isinstance(error.original, discord.Forbidden):
                self.mp_bot.description = "The bot is missing the `Ban Members` permission!" 
                await ctx.send(embed = self.mp_bot)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Ban Members` permission!"
            await ctx.send(embed = self.mp_user)
        elif isinstance(error.original, discord.Forbidden):
            self.mp_bot.description = "The bot is missing the `Ban Members` permission!" 
            await ctx.send(embed = self.mp_bot)

    @banlist.error 
    async def banlist_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Ban Members` permission!"
            await ctx.send(embed = self.mp_user)
        elif hasattr(error, 'original'):
            if isinstance(error.original, discord.Forbidden):
                self.mp_bot.description = "The bot is missing the `Ban Members` permission!" 
                await ctx.send(embed = self.mp_bot)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Manage Roles` permission!"
            await ctx.send(embed = self.mp_user)
        elif hasattr(error, 'original'):
            if isinstance(error.original, discord.Forbidden):
                self.mp_bot.description = "The bot is missing the `Manage Roles` permission!" 
                await ctx.send(embed = self.mp_bot)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Manage Roles` permission!"
            await ctx.send(embed = self.mp_user)
        elif hasattr(error, 'original'):
            if isinstance(error.original, discord.Forbidden):
                self.mp_bot.description = "The bot is missing the `Manage Roles` permission!" 
                await ctx.send(embed = self.mp_bot)

def setup(bot):
    bot.add_cog(Mod(bot))
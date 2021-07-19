import discord 
from discord.ext import commands 

class Mod(commands.Cog):
    '''
    This command category contains all the moderator commands.
    '''
    def __init__(self, bot):
        self.bot = bot 
        self.mp_user = discord.Embed(title = ':no_entry: Permission denied! :no_entry:', color = discord.Colour.red())
        self.mp_bot = discord.Embed(title = ':warning: Bot has missing perms! :warning:', color = discord.Colour.red())

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        '''
        Kicks a member.
        '''
        embd = discord.Embed(title = f':mechanical_leg: Kicked {member.name}#{member.discriminator} :mechanical_leg:', color = 0xFFFF)
        if reason is None:
            await member.kick(reason = "Didn't provide a reason.")
            await ctx.send(embed = embd)
        else:
            await member.kick(reason = reason)
            await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        '''
        Bans a member.
        '''
        embd = discord.Embed(title = f':hammer: Banned {member.name}#{member.discriminator} :hammer:', color = 0xFFFF)
        if reason is None:
            await member.ban(reason = "Didn't provide a reason.")
            await ctx.send(embed = embd)
        else:
            await member.ban(reason = reason)
            await ctx.send(embed = embd)

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
        message = await ctx.send('Hold on this may take a while.')
        banlist_embed = discord.Embed(title = f'Banned members in {ctx.guild}:', color = 0xFFFF)

        for ban_entry in ban_list:
            user = ban_entry.user
            bans_label += f'{user.name}#{user.discriminator}\n'
        await message.delete()
        banlist_embed.description = f'```{bans_label}```'
        
        if bans_label == '':
            await ctx.send('Looks like I found no banned members.')
        else:
            await ctx.send(embed = banlist_embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member):
        '''
        Mutes a member in both text and voice channels.
        '''
        # data = self.server_data
        # embd = discord.Embed(title = f'{member.name} has been muted', color = discord.Colour.purple())
        # mute_role = data[str(ctx.guild.id)]['mute_role']
        # if mute_role != None:
        #     member.add_roles(ctx.guild.get_role(mute_role))
        #     await ctx.send(embed = embd)
        # else:
        #     await ctx.reply("The bot doesn't know which mute role to add, have you tried the $add-mute-role command?")
        await ctx.send('This command is under maintenance.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: discord.Member):
        '''
        Unmutes a member in both text and voice channels.
        '''
        # data = self.server_data
        # embd = discord.Embed(title = f'{member.name} has been unmuted.', color = discord.Colour.orange())
        # mute_role = data[str(ctx.guild.id)]['mute_role']
        # if member.guild.get_role(mute_role) in member.roles:
        #     await member.remove_roles(ctx.guild.get_role(mute_role)) 
        #     await ctx.send(embed = embd)
        # else:
        #     await ctx.reply('Member is not muted.')
        await ctx.send('This command is under maintenance.')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            self.mp_user.description = "You are missing the `Kick Members` permission!"
            await ctx.send(embed = self.mp_user)
        elif isinstance(error, discord.Forbidden):
            self.mp_bot.description = "The bot is missing the `Kick Members` permission!" 
            await ctx.send(embed = self.mp_bot)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Ban Members` permission!"
            await ctx.send(embed = self.mp_user)
        elif isinstance(error, discord.Forbidden):
            self.mp_bot.description = "The bot is missing the `Ban Members` permission!" 
            await ctx.send(embed = self.mp_bot)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Ban Members` permission!"
            await ctx.send(embed = self.mp_user)
        elif isinstance(error, discord.Forbidden):
            self.mp_bot.description = "The bot is missing the `Ban Members` permission!" 
            await ctx.send(embed = self.mp_bot)

    @banlist.error 
    async def banlist_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Ban Members` permission!"
            await ctx.send(embed = self.mp_user)
        elif isinstance(error, discord.Forbidden):
            self.mp_bot.description = "The bot is missing the `Ban Members` permission!" 
            await ctx.send(embed = self.mp_bot)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Manage Roles` permission!"
            await ctx.send(embed = self.mp_user)
        elif isinstance(error, discord.Forbidden):
            self.mp_bot.description = "The bot is missing the `Manage Roles` permission!" 
            await ctx.send(embed = self.mp_bot)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            self.mp_user.description = "You are missing the `Manage Roles` permission!"
            await ctx.send(embed = self.mp_user)
        elif isinstance(error, discord.Forbidden):
            self.mp_bot.description = "The bot is missing the `Manage Roles` permission!" 
            await ctx.send(embed = self.mp_bot)

def setup(bot):
    bot.add_cog(Mod(bot))
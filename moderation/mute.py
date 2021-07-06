import discord
from discord.ext import commands
from noncoroutines import get_json_data

class Mute(commands.Cog):
    '''
    Commands related to muting members from guild.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.server_data = get_json_data('data.json')
        self.mp_mute = discord.Embed(title = ':no_entry: Permission denied! :no_entry:', description = 'You are missing the `Manage Roles` permission!', color = discord.Colour.red())

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member):
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
        # data = self.server_data
        # embd = discord.Embed(title = f'{member.name} has been unmuted.', color = discord.Colour.orange())
        # mute_role = data[str(ctx.guild.id)]['mute_role']
        # if member.guild.get_role(mute_role) in member.roles:
        #     await member.remove_roles(ctx.guild.get_role(mute_role))
        #     await ctx.send(embed = embd)
        # else:
        #     await ctx.reply('Member is not muted.')
        await ctx.send('This command is under maintenance.')
        
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_mute)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_mute)

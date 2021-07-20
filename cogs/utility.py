import discord 
from discord.ext import commands 

class Utility(commands.Cog):
    '''
    This command category contains all useful commands.
    '''
    
    def __init__(self, bot):
        self.bot = bot
        self.pong_url = 'https://media1.tenor.com/images/d43fa1f8705692a7907cf3952fd322e4/tenor.gif?itemid=14393751'

    @commands.command()
    async def ping(self, ctx):
        '''
        Returns the latency of the bot
        '''
        embd = discord.Embed(title = 'Pong!', color = 0xFFFF)
        embd.set_thumbnail(url = self.pong_url)
        embd.add_field(name = 'Latency:', value = f'`{self.bot.latency * 1000:.2f}ms`')

        await ctx.send(embed = embd)

    @commands.command()
    async def botinfo(self, ctx):
        '''
        Returns info about the bot.
        '''
        bot_dev = self.bot.get_user(self.bot.owner_id)

        embd = discord.Embed(title = f'Info about: {self.bot.user.name}#{self.bot.user.discriminator}', description = self.bot.description, color = 0xFFFF)
        embd.set_thumbnail(url = self.bot.user.avatar_url)
        embd.add_field(name = 'Developer:', value = f'`{bot_dev.name}#{bot_dev.discriminator}`', inline = False)
        embd.add_field(name = 'Library used:', value = f"`Name: discord.py`\n`Version: {discord.__version__}`", inline = False)
        embd.add_field(name = 'Servers joined:', value = f'`{len(self.bot.guilds)}`', inline = False)

        await ctx.send(embed = embd)


    @commands.command() 
    @commands.guild_only()
    async def serverinfo(self, ctx):
        '''
        Returns info about the server. 
        '''
        len_text = len(ctx.guild.text_channels)
        len_voice = len(ctx.guild.voice_channels)
        len_users = len([user for user in ctx.guild.members if not user.bot])
        len_bots = len([user for user in ctx.guild.members if user.bot])
        len_emojis = len(ctx.guild.emojis)
        server_owner = self.bot.get_user(ctx.guild.owner_id)

        embd = discord.Embed(title = f'Info about: {ctx.guild}', description = f'Server description:\n{ctx.guild.description}', color = 0xFFFF) 
        embd.set_thumbnail(url = ctx.guild.icon_url)
        embd.add_field(name = 'Owner:', value = f'`Username: {server_owner.name}#{server_owner.discriminator}`\n`Id: {server_owner.id}`', inline = False)
        embd.add_field(name = 'General info:', value = f'`Server creation at: {ctx.guild.created_at}`\n`Server ID: {ctx.guild.id}`\n`Region: {ctx.guild.region}`', inline = False)
        embd.add_field(name = 'Channel count:', value = f'`Text Channels: {len_text}`\n`Voice Channels: {len_voice}`\n`Total: {len_text + len_voice}`', inline = False)
        embd.add_field(name = 'Member count:', value = f'`Users: {len_users}`\n`Bots: {len_bots}`\n`Total: {ctx.guild.member_count}`', inline = False)
        embd.add_field(name = 'Emoji count:', value = f'`Emoji limit: {ctx.guild.emoji_limit}`\n`Emojis: {len_emojis}`', inline = False)

        await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only() 
    async def memberinfo(self, ctx, user: commands.MemberConverter):
        '''
        Returns info about a member.
        '''
        pass 

    @commands.command() 
    @commands.guild_only()
    async def roleinfo(self, ctx, role: commands.RoleConverter):
        '''
        Returns info about a role.
        '''
        pass 

def setup(bot):
    bot.add_cog(Utility(bot))
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
        embd = discord.Embed(title = 'Pong!', colour = discord.Colour.green())
        embd.set_thumbnail(url = self.pong_url)
        embd.add_field(name = 'Latency:', value = f'`{self.bot.latency * 1000:.2f}ms`')
        await ctx.send(embed = embd)

    @commands.command()
    async def botinfo(self, ctx):
        '''
        Returns info about the bot.
        '''
        embd = discord.Embed()
        bot_dev = self.bot.get_user(self.bot.owner_id)
        embd.title = f'Info about: {self.bot.user.name}#{self.bot.user.discriminator}'
        embd.description = self.bot.description
        embd.colour = discord.Colour.green()
        embd.set_thumbnail(url = self.bot.user.avatar_url)
        embd.add_field(name = 'Developer:', value = f'`{bot_dev.name}#{bot_dev.discriminator}`')
        embd.add_field(name = 'Library used:', value = f"Name: `discord.py`\nVersion: `{discord.__version__}`")
        await ctx.send(embed = embd)


    @commands.command() 
    @commands.guild_only()
    async def serverinfo(self, ctx):
        '''
        Returns info about the server. 
        '''
        pass 

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
import discord 
from discord.ext import commands 
from noncoroutines import get_help_fun, get_help_mod, get_help_util_welcome, get_help_util_mute, get_help_game

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        embd = discord.Embed(title = 'Need help? Refer down below!',
                description = 'Check out the commands!',
                color = discord.Colour.green())
        embd.add_field(name = ':basketball: For fun :basketball:', value = '`$help fun`',  inline = False)
        embd.add_field(name = ':shield: For moderation :shield:',value = '`$help mod`', inline = False)
        embd.add_field(name = ':gear: For settings :gear:',value = '`$help settings`', inline = False)
        embd.add_field(name = ':video_game: Games :video_game:', value = '`$help games`', inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def fun(self, ctx):
        embd = discord.Embed(title = 'These are the commands for fun!', description = get_help_fun(), color = discord.Colour.green())
        await ctx.send(embed = embd)

    @help.command()
    async def mod(self, ctx):
        embd = discord.Embed(title = 'Moderator commands!', description = get_help_mod(), color = discord.Colour.green())
        embd.set_footer(text = "Don't forget to sync my perms for them to work!")
        await ctx.send(embed = embd)

    @help.command()
    async def settings(self, ctx):
        embd = discord.Embed(title = 'Termino utilities!', color = discord.Colour.green())
        embd.add_field(name = 'Welcomes:', value = get_help_util_welcome(), inline = False)
        embd.add_field(name = 'Mute command setup:', value = get_help_util_mute(), inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def games(self, ctx):
        embd = discord.Embed(title = 'Games!', description = get_help_game(), color = discord.Colour.green())
        await ctx.send(embed = embd)

    @help.command()
    async def display(self, ctx):
        pass 

    @help.command()
    async def randomnum(self, ctx):
        pass 

    @help.command()
    async def solve(self, ctx):
        pass 

    @help.command()
    async def randomslap(self, ctx):
        pass 

    @help.command(name = '8ball')
    async def _8ball(self, ctx):
        pass 

    @help.command()
    async def iseven(self, ctx):
        pass

    @help.command()
    async def hack(self, ctx):
        pass 

    @help.command()
    async def ban(self, ctx):
        pass 

    @help.command()
    async def kick(self, ctx):
        pass 

    @help.command()
    async def unban(self, ctx):
        pass 

    @help.command()
    async def mute(self, ctx):
        pass 

    @help.command()
    async def banlist(self, ctx):
        pass

    @help.command(name = 'set-join-role')
    async def set_join_role(self, ctx):
        pass 

    @help.command(name = 'set-join-channel')
    async def set_join_channel(self, ctx):
        pass 

    @help.command(name = 'welcome-dm-message')
    async def set_dm_message(self, ctx):
        pass 

    @help.command(name = 'add-mute-role')
    async def add_mute_role(self, ctx):
        pass 

    @help.command(aliases = ['rock-paper-scissors','rps'])
    async def rock_paper_scissors(self, ctx):
        pass 

    @help.command()
    async def dice(self, ctx):
        pass 

def setup(bot):
    bot.add_cog(Help(bot))
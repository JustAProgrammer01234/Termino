import discord 
from discord.ext import commands 

class Voice(commands.Cog, name = 'voice'):
    '''
    This category contains commands for voice channels.
    '''
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def join(self, ctx):
        '''
        Joins the voice channel your in.
        '''
        voice = ctx.author.voice
        if voice != None:
            await voice.channel.connect()
            join_embed = discord.Embed(description = f"**Successfully connected to {voice.channel.mention}.**", colour = discord.Colour.green())
        else:
            join_embed = discord.Embed(description = f"**Please join a voice channel.**", colour = discord.Colour.red())
        await ctx.send(embed = join_embed)

    @commands.command()
    async def leave(self, ctx):
        '''
        Leaves the voice channel the bot is in.
        '''
        voice = ctx.voice_client 
        if voice != None:
            await voice.disconnect()
            leave_embed = discord.Embed(description = f"**Successfully left to {voice.channel.mention}.**", colour = discord.Colour.green())
        else:
            leave_embed = discord.Embed(description = f"**Can't disconnect, I'm not currently in a voice channel.**", colour = discord.Colour.red())
        await ctx.send(embed = leave_embed)


def setup(bot):
    bot.add_cog(Voice(bot))
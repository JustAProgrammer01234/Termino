import discord
from discord.ext import commands 
from .util import imageutil

class Image(commands.Cog):
    '''
    This category contains all the commands for image manipulation.
    '''
    def __init__(self, bot):
        self.bot = bot 
        
    def __str__(self):
        return ':frame_photo: Image :frame_photo:'

    async def check_if_author(self, ctx, member):
        if member is None:
            return await ctx.author.avatar.read()
        return await member.avatar.url.read()

    @commands.command()
    @commands.guild_only()
    async def invert(self, ctx, member: commands.MemberConverter = None):
        '''
        Inverts the pfp of a member or yours.
        '''
        async with ctx.typing():
            bytes_image = await self.check_if_author(ctx, member)
            inverted_bytes = await imageutil.invert(bytes_image)
            await ctx.send(file = discord.File(fp = inverted_bytes, filename = 'inverted.png'))

    @commands.command()
    @commands.guild_only()
    async def rotate(self, ctx, degrees: float, member: commands.MemberConverter = None):
        '''
        Rotates the pfp of a member or yours by a number of degrees.
        '''
        async with ctx.typing():
            bytes_image = await self.check_if_author(ctx, member)
            rotated_bytes = await imageutil.rotate(bytes_image, degrees)
            await ctx.send(file = discord.File(fp = rotated_bytes, filename = 'rotated.png'))

    @commands.command()
    @commands.guild_only()
    async def filter(self, ctx, member: commands.MemberConverter = None):
        '''
        Filters the pfp of a member or yours.
        '''
        async with ctx.typing():
            bytes_image = await self.check_if_author(ctx, member)
            filtered_bytes = await imageutil.filter(bytes_image)
            await ctx.send(file = discord.File(fp = filtered_bytes, filename = 'filtered.png'))

    @commands.command()
    @commands.guild_only()
    async def mirror(self, ctx, member: commands.MemberConverter = None):
        '''
        "Mirrors" the pfp of a member or yours.
        '''
        async with ctx.typing():
            bytes_image = await self.check_if_author(ctx, member)
            filtered_bytes = await imageutil.mirror(bytes_image)
            await ctx.send(file = discord.File(fp = filtered_bytes, filename = 'mirrored.png'))

def setup(bot):
    bot.add_cog(Image(bot))
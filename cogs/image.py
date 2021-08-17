import discord
from discord.ext import commands 
from .util import imageutil 

class Image(commands.Cog, name = 'image'):
    '''
    This command category contains all the commands for image manipulation.
    '''
    def __init__(self, bot):
        self.bot = bot 
        
    def __repr__(self):
        return ':frame_photo: Image :frame_photo:'

    @commands.command(name = 'invert-profile')
    async def invert_profile(self, ctx, member: discord.Member = None):
        '''
        Inverts the profile of a member or yours.
        '''
        if member is None:
            avatar_url = ctx.author.avatar_url_as(format = 'png')
        else:
            avatar_url = member.avatar_url_as(format = 'png')
    
        bytes_image = await avatar_url.read()
        inverted_bytes = await imageutil.invert(bytes_image)
        await ctx.send(file = discord.File(fp = inverted_bytes, filename = 'inverted.png'))

def setup(bot):
    bot.add_cog(Image(bot))
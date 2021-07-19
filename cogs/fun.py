import string
import random
import asyncio
import discord
from .util import converters
from discord.ext import commands
from discord.ext.commands import errors

class Fun(commands.Cog):
    '''
    This category contains all the fun commands you can do.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.gif_url =[
            'https://media1.tenor.com/images/31f29b3fcc20a486f44454209914266a/tenor.gif?itemid=17942299',
            'https://media1.tenor.com/images/3c161bd7d6c6fba17bb3e5c5ecc8493e/tenor.gif?itemid=5196956',
            'https://media1.tenor.com/images/e29671457384a94a7e19fea26029b937/tenor.gif?itemid=10048943',
            'https://media1.tenor.com/images/42621cf33b44ca6a717d448b1223bccc/tenor.gif?itemid=15696850',
            'https://media1.tenor.com/images/7680952f25c4aaf8f2d04930b05da340/tenor.gif?itemid=16545760',
            'https://media1.tenor.com/images/49de17c6f21172b3abfaf5972fddf6d6/tenor.gif?itemid=10206784'
        ]

    @commands.command(aliases = ['print'])
    async def copy(self, ctx, mode, *, message):
        '''
        __**Description:**__
        Copies the message you sent in `<message>`

        __**Arguments:**__
        **1.** `<mode>` - Must be -orig if to be shown in plain text or -embd if to be shown inside an embed.
        **2.** `<mesage>` - The message to be copied
        '''

        if mode == '-orig':
            await ctx.send(message)
        elif mode == '-embd':
            embd = discord.Embed(description = message)
            await ctx.send(embed = embd)
        else:
            await ctx.send('Error: <mode> must either be -orig if you want to show just plain text, or -embd if you want to show message inside embd.')

    @commands.command()
    async def randomnum(self, ctx, start: int, stop: int):
        '''
        __**Description:**__
        Generates a random number for you from `<start>` to `<stop>`.

        __**Arguments:**__
        **1.** `<start>` - The number to start. (Must be an integer like this -> 2)
        **2.** `<stop>` - The number to stop. (Must be an integer like this -> 2)
        '''

        embd = discord.Embed(title = f'Generated random number from {start} to {stop}:',
        description = random.randint(start, stop), color = discord.Colour.green())
        await ctx.send(embed = embd)

    @commands.command()
    async def solve(self, ctx, *, equation):
        '''
        __**Description:**__
        Sends the solution for `<equation>`

        __**Arguments:**__
        **1.** `<equation>` - The equation to be solved. (Must be mdas format like this -> 1/2+1*2-1)
        '''

        await ctx.send(eval(equation))

    @commands.command(name = '8ball', aliases = ['8b','magic_ball'])
    async def _8ball(self, ctx, *, question: converters.eightball):
        '''
        __**Description:**__
        An implementation of the 8ball fortune teller.

        __**Arguments:**__
        **1.** `<question>` - The question to be answered by the 8ball command.
        '''

        embd = discord.Embed(title = '8ball says:', description = question[0], color = discord.Colour.green())
        embd.set_thumbnail(url = 'https://magic-8ball.com/assets/images/magicBallStart.png')
        embd.set_footer(text = f'Question: {question[1]}')
        await ctx.send(embed = embd)

    @commands.command()
    async def iseven(self, ctx, number: converters.is_even):
        '''
        __**Description:**__
        Tells you if `<number>` is even or not.

        __**Arguments:**__
        **1.** `<number>` - The number to be checked. (Must be an integer like this -> 2)
        '''

        await ctx.send(number)

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx, member: discord.Member, *, reason):
        '''
        __**Description:**__
        Slaps a specific member in a discord server.

        __**Arguments:**__
        **1.** `<member>` - The member to be slapped. (This argument must only contain a member id or a ping.)
        **2.** `<reason>` - The reason you slapped that member.
        '''

        embd = discord.Embed(description = f'{ctx.author.mention} slapped {member.mention} because of **{reason}**', color = discord.Colour.green())
        embd.set_image(url = random.choice(self.gif_url))
        await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    async def randomslap(self, ctx, *, reason: converters.SlapSomeone):
        '''
        __**Description:**__
        Randomly slaps a member in a discord server.

        __**Arguments:**__
        **1.** `<reason>` - The reason you slapped that member.
        '''

        embd = discord.Embed(description = reason, color = discord.Colour.green())
        embd.set_image(url = random.choice(self.gif_url))
        await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    async def hack(self, ctx, member: discord.Member):
        '''
        __**Description:**__
        A command that hacks a member. (This is not meant to be real so don't worry if you get hacked by this.)

        __**Arguments:**__
        **1.** `<member>` - The member to be slapped. (This argument must only contain a member id or a ping.)
        '''

        password_chars = [char for char in string.ascii_letters + string.digits + string.punctuation]
        password_length = random.randint(5,10)
        password = [random.choice(password_chars) for _ in range(password_length)]
        hack_message = await ctx.send(f'Hacking {member.mention}')
        hack_embed_message = discord.Embed(description = f'Credentials of {member.mention}', color = discord.Colour.red())
        hack_embed_message.add_field(name = 'Ip address:', value = f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}', inline = False)
        hack_embed_message.add_field(name = 'Email:', value = f'{member.name}@gmail.com', inline = False)
        hack_embed_message.add_field(name = 'Password:',value = f"{''.join(password)}", inline = False)
        hack_embed_message.set_thumbnail(url = member.avatar_url)
        hack_embed_message.set_footer(text = f'Hacked by: {ctx.message.author}', icon_url = ctx.message.author.avatar_url)
        message_dict = {0: 'Found ip', 1: 'Found email',2: 'Found email password'}
        for i in range(3):
            await asyncio.sleep(1)
            await hack_message.edit(content = message_dict[i])
        await asyncio.sleep(1)
        await hack_message.delete()
        await ctx.send(embed = hack_embed_message)

def setup(bot):
    bot.add_cog(Fun(bot))
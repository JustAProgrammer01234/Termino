import string
import asyncio
import discord
from discord.ext import commands
from .util import reddit, corefuncs

gif_url = [
        'https://media1.tenor.com/images/31f29b3fcc20a486f44454209914266a/tenor.gif?itemid=17942299',
        'https://media1.tenor.com/images/3c161bd7d6c6fba17bb3e5c5ecc8493e/tenor.gif?itemid=5196956',
        'https://media1.tenor.com/images/e29671457384a94a7e19fea26029b937/tenor.gif?itemid=10048943',
        'https://media1.tenor.com/images/42621cf33b44ca6a717d448b1223bccc/tenor.gif?itemid=15696850',
        'https://media1.tenor.com/images/7680952f25c4aaf8f2d04930b05da340/tenor.gif?itemid=16545760',
        'https://media1.tenor.com/images/49de17c6f21172b3abfaf5972fddf6d6/tenor.gif?itemid=10206784'
    ]

eightball_messages = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't count on it.",
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Replay hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.'
        ]

class Fun(commands.Cog, name = 'fun'):
    '''
    This category contains all the fun commands you can do.
    '''
    def __init__(self, bot):
        self.bot = bot

    def __repr__(self):
        return '> Fun :basketball:'

    @commands.command()
    async def randomnum(self, ctx, start: int, stop: int):
        '''
        Generates a random number for you from `<start>` to `<stop>`.
        '''
        try:
            embd = discord.Embed(title = f'Generated random number from {start} to {stop}:',
            description = f'`{await corefuncs.generate_random_number(start, stop)}`', color = discord.Colour.from_rgb(255,255,255))
            await ctx.send(embed = embd) 
        except ValueError:
            await ctx.send("The first number must be less than the other.")

    @commands.command(name = '8ball', aliases = ['8b','magic_ball'])
    async def _8ball(self, ctx, *, question):
        '''
        An implementation of the 8ball fortune teller.
        '''
        random_response = await corefuncs.random_choice(eightball_messages)
        embd = discord.Embed(title = '8ball says:', description = f'```{random_response}```', color = discord.Colour.from_rgb(255,255,255))
        embd.set_thumbnail(url = 'https://magic-8ball.com/assets/images/magicBallStart.png')
        embd.set_footer(text = f'Question: {question}')
        await ctx.send(embed = embd)

    @commands.command()
    async def iseven(self, ctx, number: int):
        '''
        Tells you if `<number>` is even or not.
        '''
        if number % 2 == 0:
            await ctx.send(f"Number {number} is even.")
        else:
            await ctx.send(f"Number {number} is not even.")

    @commands.command()
    async def meme(self, ctx):
        '''
        Sends a random meme from r/memes
        '''
        meme = await self.bot.reddit.get_random_post('memes')
        meme_embed = discord.Embed(title = meme[0], url = meme[3], color = discord.Colour.from_rgb(255,255,255))
        meme_embed.set_author(name = f'Meme by: u/{meme[1]}')
        meme_embed.set_image(url = meme[2])
        meme_embed.set_footer(text = f'Upvotes: {meme[4]}')
        await ctx.send(embed = meme_embed)
    
    @commands.command()
    async def okand(self, ctx):
        '''
        Ok, and?
        '''
        await ctx.send("Ok, and?")

    @commands.command()
    async def nooneasked(self, ctx):
        '''
        No one asked.
        '''
        await ctx.send("No one asked, mate.")

    @commands.command(name = 'check-luck')
    @commands.guild_only()
    async def check_luck(self, ctx, member: commands.MemberConverter = None):
        '''
        Checks how lucky you are or how lucky a member is.
        '''
        luck = await corefuncs.generate_random_number(1, 100)
        luck_embed = discord.Embed(description = f":four_leaf_clover: `{luck}%` :four_leaf_clover:", colour = discord.Colour.from_rgb(255,255,255))

        if member is None:
            luck_embed.title = 'Your luck is:'
        else:
            luck_embed.title = f'The luck of {member.name} is:'

        await ctx.send(embed = luck_embed)

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx, member: commands.MemberConverter, *, reason):
        '''
        Slaps a specific member in a discord server.
        '''
        embd = discord.Embed(description = f'{ctx.author.mention} slapped {member.mention} because of **{reason}**', color = discord.Colour.from_rgb(255,255,255))
        embd.set_image(url = await corefuncs.random_choice(gif_url))
        await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    async def randomslap(self, ctx, *, reason):
        '''
        Slaps a random member in a discord server.
        '''
        random_member = await corefuncs.random_choice(ctx.guild.members)
        embd = discord.Embed(description = f'{ctx.author.mention} slapped {random_member.mention} because of **{reason}**.', color = discord.Colour.from_rgb(255,255,255))
        embd.set_image(url = await corefuncs.random_choice(gif_url))
        await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    async def hack(self, ctx, member: commands.MemberConverter):
        '''
        A command that hacks a member. (This is not meant to be real so don't worry if you get hacked by this.)
        '''
        password_chars = [char for char in string.ascii_letters + string.digits + string.punctuation]
        password_length = await corefuncs.generate_random_number(5,10)
        password = [await corefuncs.random_choice(password_chars) for _ in range(password_length)]
        hack_message = await ctx.send(f'Hacking {member.mention}')
        hack_embed_message = discord.Embed(title = f'Credentials of {member}', color = discord.Colour.from_rgb(255,255,255))
        hack_embed_message.add_field(name = 'Ip address:', value = f'{await corefuncs.generate_random_number(0, 255)}.{await corefuncs.generate_random_number(0, 255)}.{await corefuncs.generate_random_number(0, 255)}.{await corefuncs.generate_random_number(0, 255)}', inline = False)
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
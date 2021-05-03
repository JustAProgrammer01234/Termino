import random
import discord
import moderation
from converters import *
from discord.ext import commands
from noncoroutines.funcs import *
from discord.ext.commands.errors import *

intents = discord.Intents.all()
termino = commands.Bot(command_prefix = '$', help_command = None, intents = intents)

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.reply('Error: Command not found')

@termino.command()
async def help(ctx):
    embd = discord.Embed(title = 'Need help? Refer down below!',
            description = get_help())
    await ctx.reply(embed = embd)

@termino.command()
async def display(ctx, mode, *, message):
    if mode == '-orig':
        await ctx.reply(message)
    elif mode == '-embd':
        embd = discord.Embed(description = message)
        await ctx.reply(embed = embd)
    else:
        await ctx.reply('Error: <mode> must either be -orig if you want to show just plain text, or -embd if you want to show message inside embed.')
    
@termino.command()
async def randomnum(ctx, start: int, stop: int):
    embd = discord.Embed(title = 'Generated random number:',
            description = f'{random.randint(start, stop)}')
    await ctx.reply(embed = embd)

@termino.command()
async def add(ctx, addend1: float, addend2: float):
    embd = discord.Embed(title = f'The sum of {addend1} and {addend2} is:',
        description = f'{addend1 + addend2}')
    await ctx.reply(embed = embd)

@termino.command()
async def source(ctx):
    embd = discord.Embed(title = "I'm glad you want to see how I was built. Click the link below to see my source code!",
            description = 'https://github.com/JustAProgrammer01234/Termino',)
    await ctx.reply(embed = embd)

@termino.command()
async def randomslap(ctx,*, reason: SlapSomeone):
    embd = discord.Embed(description = reason)
    embd.set_image(url = "https://media1.tenor.com/images/8b80166ce48c9c198951361715a90696/tenor.gif?itemid=4575896")
    await ctx.send(embed = embd)

@termino.command(name = '8ball')
async def _8ball(ctx, *, answer: eightball):
    embd = discord.Embed(title = '8ball says:', 
            description = answer[0]) 
    embd.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/9/90/Magic8ball.jpg')
    embd.set_footer(text = f'Question: {answer[1]}')
    await ctx.reply(embed = embd)

@termino.command()
async def iseven(ctx, number: is_even):
    await ctx.reply(number)

@termino.command()
async def slap(ctx, member: discord.Member, *, reason):
    embd = discord.Embed(description = f"**{ctx.author.mention} slapped {member.mention} because of {reason}.**")
    embd.set_image(url = "https://media1.tenor.com/images/0480faa72a67ba6cdd3bc87de26c819d/tenor.gif?itemid=16545714")
    await ctx.send(embed = embd)


moderation.add_command(termino)
termino.run(get_token())

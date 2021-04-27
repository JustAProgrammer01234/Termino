import random
import discord
import moderation
from converters import *
from discord.ext import commands
from noncoroutines.funcs import *

intents = discord.Intents.all()
termino = commands.Bot(command_prefix = '$', help_command = None, intents = intents)

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.command()
async def help(ctx):
    embd = discord.Embed(title = 'Need help? Refer down below!',
            description = get_help())
    await ctx.send(embed = embd)

@termino.command()
async def display(ctx,*, message):
    embd = discord.Embed(description = message)
    await ctx.send(embed = embd)

@termino.command()
async def randomnum(ctx, start: int, stop: int):
    embd = discord.Embed(title = 'Generated random number:',
            description = f'{random.randint(start, stop)}')
    await ctx.send(embed = embd)

@termino.command()
async def add(ctx, addend1: float, addend2: float):
    embd = discord.Embed(title = f'The sum of {addend1} and {addend2} is:',
        description = f'{addend1 + addend2}')
    await ctx.send(embed = embd)

@termino.command()
async def source(ctx):
    embd = discord.Embed(title = "I'm glad you want to see how I was built, click the link below to see my source code!",
            description = 'https://github.com/JustAProgrammer01234/Termino',)
    await ctx.send(embed = embd)

@termino.command()
async def slap(ctx,*, reason: SlapSomeone):
    embd = discord.Embed(description = reason)
    await ctx.send(embed = embd)

@termino.command(aliases = ['8ball','fortune_teller'])
async def _8ball(ctx, *, answer: eightball):
    embd = discord.Embed(description = answer)
    await ctx.send(embed = embd)

@termino.command()
async def iseven(ctx, number: is_even):
    embd = discord.Embed(description = number)
    await ctx.send(embed = embd)

moderation.add_command(termino)
termino.run(get_token())

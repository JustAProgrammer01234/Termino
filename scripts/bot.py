import random
import discord
from discord.ext import commands
from noncoroutines.funcs import *
from converters.converters import *
from converters.advancedconverters import *

intents = discord.Intents.all()
termino = commands.Bot(command_prefix = '$', help_command = None, intents = intents)

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.command()
async def help(ctx):
    await ctx.send(get_help())

@termino.command()
async def display(ctx,*, message):
    await ctx.send(message)

@termino.command()
async def randomnum(ctx, start: int, stop: int):
    await ctx.send(f'Generated random number: {random.randint(start, stop)}')

@termino.command()
async def add(ctx, addend1: float, addend2: float):
    await ctx.send(addend1 + addend2)

@termino.command()
async def source(ctx):
    await ctx.send('https://github.com/JustAProgrammer01234/Termino')

@termino.command()
async def slap(ctx, reason: SlapSomeone):
    await ctx.send(reason)

@termino.command(aliases = ['8ball','fortune_teller'])
async def _8ball(ctx, *, answer: eightball):
    await ctx.send(f'{answer}')

termino.run(get_token())

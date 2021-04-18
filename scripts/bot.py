import random
import discord
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
async def version(ctx):
    await ctx.send('Version 1.0')

@termino.command()
async def slap(ctx, reason: SlapSomeone):
    await ctx.send(reason)

termino.run(get_token())

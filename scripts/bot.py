import time
import random
from discord.ext import commands
from noncoroutines.funcs import *

termino = commands.Bot(command_prefix = '$', help_command = None)

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.command()
async def bubble_sort(ctx, array, mode):
    array = str_to_array(array)
    if len(array) <= 10:
            if mode == 'ascending':
                elapsed = run_bubble_sort_ascending(array)
                await ctx.send(f'Finished sorting array: {array} in {elapsed} seconds.')

            elif mode == 'descending':
                elapsed = run_bubble_sort_descending(array)
                await ctx.send(f'Finished sorting array: {array} in {elapsed} seconds.')

            else:
                await ctx.send(f'Error:\nWrong value of mode: {mode}\nMust be ascending or descending.')
    else:
        await ctx.send('Length of array must not be greater than ten.')


@termino.command()
async def insertion_sort(ctx, array, mode):
    array = str_to_array(array)
    if len(array) <= 10:
        if mode == 'ascending':
            elapsed = run_insertion_sort_ascending(array)
            await ctx.send(f'Finished sorting array: {array} in {elapsed} seconds.')

        elif mode == 'descending':
            elapsed = run_insertion_sort_descending(array)
            await ctx.send(f'Finished sorting array: {array} in {elapsed} seconds.')

        else:
            await ctx.send(f'Error: wrong value of mode: {mode}\nMust be ascending or descending.')
    else:
        await ctx.send('Length of array must not be greater than ten.')

@termino.command()
async def help(ctx):
    await ctx.send(get_help())

@termino.command()
async def display(ctx, message):
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

termino.run(get_token())

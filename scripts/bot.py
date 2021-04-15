import time
import random
from noncoroutines import *
from discord.ext import commands

termino = commands.Bot(command_prefix = '$', help_command = None)

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.command()
async def bubble_sort(ctx, array, mode):
    array = str_to_array(array)

    if len(array) < 10:
        if mode == 'ascending':

            start = time.time()
            bubble_sort_ascending(array)
            finish = time.time()
            elapsed = finish - start
            await ctx.send(f'Finished sorting array: {array} in {elapsed:.2f} seconds.')

        elif mode == 'descending':

            start = time.time()
            bubble_sort_descending(array)
            finish = time.time()
            elapsed = finish - start
            await ctx.send(f'Finished sorting array: {array} in {elapsed:.2f} seconds.')

        else:
            await ctx.send(f'Error: wrong value of mode: {mode}\nMust be ascending or descending.')
    else:
        await ctx.send('Length of array must not be greater than ten.')

@termino.command()
async def insertion_sort(ctx, array, mode):
    array = str_to_array(array)

    if len(array) < 10:
        if mode == 'ascending':

            start = time.time()
            insertion_sort_ascending(array)
            finish = time.time()
            elapsed = finish - start
            await ctx.send(f'Finished sorting array: {array} in {elapsed:.2f} seconds.')

        elif mode == 'descending':

            start = time.time()
            insertion_sort_descending(array)
            finish = time.time()
            elapsed = finish - start
            await ctx.send(f'Finished sorting array: {array} in {elapsed:.2f} seconds.')

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
async def randomnum(ctx, start, stop):
    await ctx.send(f'Generated random number: {random.randint(int(start), int(stop))}')

@termino.command()
async def add(ctx, addend1, addend2):
    await ctx.send(float(addend1) + float(addend2))

@termino.command()
async def source(ctx):
    await ctx.send('https://github.com/JustAProgrammer01234/Termino')

@termino.command()
async def version(ctx):
    await ctx.send('Version 1.0')

termino.run(get_token())

#!/usr/bin/env python3
import time
import random
import discord
from noncoroobj import *
from discord.ext import commands

termino = commands.Bot(command_prefix = '$', help_command = None)

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.command()
async def help(ctx):
    with open('help.txt','r') as help_message:
        await ctx.send(help_message.read())

@termino.command()
async def bubble_sort(ctx, array, mode):
    array = str_to_array(array)

    if mode == 'ascending':

        index = 1
        start = time.time()
        bubble_sort_ascending(array)
        finish = time.time()
        elapsed = finish - start
        await ctx.send(f'Finished sorting array: {array} in {elapsed:.2f} seconds.')

    elif mode == 'descending':
    
        index = 1
        start = time.time()
        bubble_sort_descending(array)
        finish = time.time()
        elapsed = finish - start
        await ctx.send(f'Finished sorting array: {array} in {elapsed:.2f} seconds.')
        
    else:
        await ctx.send(f'Error: wrong value of mode: {mode}\nMust be ascending or descending.')


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
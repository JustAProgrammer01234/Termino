#!/usr/bin/env python3
import random
import discord
from discord.ext import commands

termino = commands.Bot(command_prefix = '$', help_command = None)

def get_token():
    with open('token.txt','r') as f:
        return f.read()

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.command()
async def help(ctx):
    with open('help.txt','r') as help_message:
        await ctx.send(help_message.read())

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
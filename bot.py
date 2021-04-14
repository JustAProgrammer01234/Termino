#!/usr/bin/env python3
import random
from discord.ext import commands

termino = commands.Bot(command_prefix = '$', description = "Not yet fit for a moderator..")

def get_token():
    with open('token.txt','r') as f:
        return f.read()

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.event
async def on_member_join(member):
    print(f'{member} has joined this server!')

@termino.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

@termino.command()
async def helpme(ctx):
    with open('help.txt','r') as help_message:
        await ctx.send(help_message.read())

@termino.command()
async def copy(ctx, message):
    await ctx.send(message)

@termino.command()
async def randomnum(ctx, start, stop):
    await ctx.send(f'Generated random number: {random.randint(int(start), int(stop))}')

@termino.command()
async def add(ctx, addend1, addend2):
    await ctx.send(float(addend1) + float(addend2))

termino.run(get_token())
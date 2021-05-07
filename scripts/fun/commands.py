import random
import discord
from converters import *
from discord.ext import commands

@commands.command(aliases = ['disp'])
async def display(ctx, mode, *, message):
    if mode == '-orig':
        await ctx.send(message)
    elif mode == '-embd':
        embd = discord.Embed(description = message)
        await ctx.send(embed = embd)
    else:
        await ctx.send('Error: <mode> must either be -orig if you want to show just plain text, or -embd if you want to show message inside embd.')

@commands.command()
async def randomnum(ctx, start: int, stop: int):
    embd = discord.Embed(title = f'Generated random number from {start} to {stop}:',
            description = random.randint(start, stop))
    await ctx.send(embed = embd)

@commands.command()
async def add(ctx, addend1: float, addend2: float):
    embd = discord.Embed(title = f'The sum of {addend1} and {addend2} is:',
            description = addend1 + addend2)
    await ctx.reply(embed = embd)

@commands.command()
async def source(ctx):
    await ctx.reply('https://github.com/JustAProgrammer01234/Termino')

@commands.command()
async def randomslap(ctx, *, reason: SlapSomeone):
    embd = discord.Embed(description = reason)
    embd.set_image(url = 'https://media1.tenor.com/images/49de17c621172b3abfaf5972fddf6d6/tenor.gif?itemid=10206784')
    await ctx.send(embed = embd)

@commands.command(aliases = ['8ball', '8b'])
async def _8ball(ctx, *, answer: eightball):
    embd = discord.Embed(title = '8ball says:',
            description = answer[0])
    embd.set_thumbnail(url = 'https://magic-8ball.com/assets/images/magicBallStart.png')
    embd.set_footer(text = f'Question: {answer[1]}')
    await ctx.reply(embed = embd)

@commands.command()
async def iseven(ctx, number: is_even):
    await ctx.reply(number)

@commands.command()
async def slap(ctx, member: discord.Member, *, reason):
    embd = discord.Embed(description = f'**{ctx.author.mention} slapped {member.mention} because of {reason}**')
    embd.set_image(url = 'https://media1.tenor.com/images/0480faa72a67ba6cdd3bc87de26c819d/tenor.gif?itemid=16545714')
    await ctx.send(embed = embd)

def add_command(bot):
    bot.add_command(display)
    bot.add_command(randomnum)
    bot.add_command(add)
    bot.add_command(source)
    bot.add_command(randomslap)
    bot.add_command(_8ball)
    bot.add_command(iseven)
    bot.add_command(slap)

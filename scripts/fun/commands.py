import string
import random
import asyncio
import discord
from converters import *
from discord.ext import commands

gif_url = [
    'https://media1.tenor.com/images/31f29b3fcc20a486f44454209914266a/tenor.gif?itemid=17942299',
    'https://media1.tenor.com/images/3c161bd7d6c6fba17bb3e5c5ecc8493e/tenor.gif?itemid=5196956',
    'https://media1.tenor.com/images/e29671457384a94a7e19fea26029b937/tenor.gif?itemid=10048943',
    'https://media1.tenor.com/images/42621cf33b44ca6a717d448b1223bccc/tenor.gif?itemid=15696850',
    'https://media1.tenor.com/images/7680952f25c4aaf8f2d04930b05da340/tenor.gif?itemid=16545760',
    'https://media1.tenor.com/images/49de17c6f21172b3abfaf5972fddf6d6/tenor.gif?itemid=10206784'
]

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
async def solve(ctx, *, equation):
    await ctx.reply(eval(equation))

@commands.command()
async def randomslap(ctx, *, reason: SlapSomeone):
    embd = discord.Embed(description = reason)
    embd.set_image(url = random.choice(gif_url))
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
    embd.set_image(url = random.choice(gif_url))
    await ctx.send(embed = embd)

@commands.command()
async def hack(ctx, member: discord.Member):
    password_chars = [char for char in string.ascii_letters + string.digits + string.punctuation]
    password_length = random.randint(5,10)
    password = [random.choice(password_chars) for _ in range(password_length)]
    hack_message = await ctx.send(f'Hacking {member.mention}')
    hack_embed_message = discord.Embed(description = f'Credentials of {member.mention}', color = discord.Colour.red())
    hack_embed_message.add_field(name = 'Ip address:', value = f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}', inline = False)
    hack_embed_message.add_field(name = 'Email:', value = f'{member.name}@gmail.com', inline = False)
    hack_embed_message.add_field(name = 'Password:',value = f"{''.join(password)}", inline = False)
    hack_embed_message.set_thumbnail(url = member.avatar_url)
    hack_embed_message.set_footer(text = f'Hacked by: {ctx.message.author}', icon_url = ctx.message.author.avatar_url)
    message_dict = {0: 'Found ip', 1: 'Found email',2: 'Found email password'}
    for i in range(3):
        await asyncio.sleep(1)
        await hack_message.edit(content = message_dict[i])
    await asyncio.sleep(1)
    await hack_message.edit(embed = hack_embed_message)

@commands.command()
async def dice(ctx):
    player_dice = random.randint(1,6)
    bot_dice = random.randint(1,6)
    embed_color = random.randint(0x000000, 0xffffff)
    if player_dice == bot_dice:
        result_message = "Looks like it's a tie man."
    elif player_dice > bot_dice:
        result_message = 'Oh, looks like you won.'
    else:
        result_message = "Hahahah loser I won."
    result_embed = discord.Embed(title = result_message, color = embed_color)
    result_embed.add_field(name = 'You:', value = player_dice, inline = True)
    result_embed.add_field(name = 'Termino:', value = bot_dice, inline = True)
    await ctx.send(embed = result_embed)


def add_command(bot):
    bot.add_command(display)
    bot.add_command(randomnum)
    bot.add_command(solve)
    bot.add_command(randomslap)
    bot.add_command(_8ball)
    bot.add_command(iseven)
    bot.add_command(slap)
    bot.add_command(hack)
    bot.add_command(dice)

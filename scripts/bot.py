import fun
import random
import discord
import moderation
from converters import *
from discord.errors import *
from discord.ext import commands
from noncoroutines.funcs import *
from discord.ext.commands.errors import *

intents = discord.Intents.all()
termino = commands.Bot(command_prefix = '$', help_command = None, intents = intents)

@termino.event
async def on_ready():
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.reply('Error: Command not found')
    elif isinstance(error, MissingPermissions):
        await ctx.reply('Error: Permission Denied')
    elif isinstance(error, Forbidden):
        await ctx.reply('Error: I do not have permissions to do that command.')
    else:
        #for debugging purposes
        print(error)

@termino.command()
async def help(ctx, cmd_category = None):
    if cmd_category == None:
        embd = discord.Embed(title = 'Need help? Refer down below!',
                description = get_help())
    elif cmd_category == 'fun':
        embd = discord.Embed(title = 'These are the commands for fun!',
                description = get_help_fun())
        embd.set_footer(text = 'Hope you have fun lmfao')
    elif cmd_category == 'moderation':
        embd = discord.Embed(title = 'These are the commands for discord mods to use!',
                description = get_help_mod())
        embd.set_footer(text = 'Still in development!')
    await ctx.reply(embed = embd)

fun.add_command(termino)
moderation.add_command(termino)

termino.run(get_token())

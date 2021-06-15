import fun
import util
import random
import discord
import moderation
from discord.ext import commands
from noncoroutines.funcs import *
from discord.errors import Forbidden
from discord.ext.commands.errors import CommandNotFound, MissingPermissions, NoPrivateMessage

intents = discord.Intents.all()
termino = commands.Bot(command_prefix = '$', help_command = None, intents = intents)

@termino.event
async def on_ready():
    await termino.change_presence(activity = discord.Game(name = 'for $help'))
    print(f'{termino.user.name} is ready to go.')
    print('-----------------------------------')

@termino.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.reply("Well, couldn't find that command mate. Try typing $help so you would know.")
    elif isinstance(error, Forbidden):
        await ctx.reply('Error: I do not have permissions to do that command.')
    elif isinstance(error, NoPrivateMessage):
        await ctx.reply('That command cannot be used in dm.')
    else:
        #for debugging purposes
        print(error)

@termino.command()
async def help(ctx, cmd_category = None):
    invite_link = get_invite_link()
    if cmd_category == None:
        embd = discord.Embed(title = 'Need help? Refer down below!',
                description = 'Check out the commands!',
                color = discord.Colour.blue())
        embd.add_field(name = ':basketball: For fun :basketball:', value = '`$help fun`',  inline = False)
        embd.add_field(name = ':shield: For moderation :shield:',value = '`$help mod`', inline = False)
        embd.add_field(name = ':gear: For utility :gear:',value = '`$help util`', inline = False)
        embd.add_field(name = ':video_game: Games :video_game:', value = '`$help games`', inline = False)
        await ctx.send(embed = embd)
    elif cmd_category == 'fun':
        embd = discord.Embed(title = 'These are the commands for fun!', description = get_help_fun(), color = discord.Colour.blue())
        await ctx.send(embed = embd)
    elif cmd_category == 'mod':
        embd = discord.Embed(title = 'Moderator commands!', description = get_help_mod(), color = discord.Colour.blue())
        embd.set_footer(text = "Don't forget to sync my perms for them to work!")
        await ctx.send(embed = embd)
    elif cmd_category == 'util':
        embd = discord.Embed(title = 'Termino utilities!', color = discord.Colour.blue())
        embd.add_field(name = 'Welcomes:', value = get_help_util_welcome(), inline = False)
        embd.add_field(name = 'Mute command setup:', value = get_help_util_mute(), inline = False)
        await ctx.send(embed = embd)
    elif cmd_category == 'games':
        embd = discord.Embed(title = 'Games!', description = get_help_game(), color = discord.Colour.blue())
        await ctx.send(embed = embd)
    else:
        await ctx.send('Command category does not exist bro.')

fun.setup(termino)
moderation.setup(termino)
util.setup(termino)

termino.run(get_token('token.txt'))

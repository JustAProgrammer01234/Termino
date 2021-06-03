import fun
import random
import discord
import moderation
from converters import *
from discord.ext import commands
from noncoroutines.funcs import *
from discord.errors import Forbidden
from discord.ext.commands.errors import CommandNotFound, MissingPermissions

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
    elif isinstance(error, MissingPermissions):
        await ctx.reply('Bro you do not have permissions to do that command. Try contacting the staff of this server or something I dunno.')
    elif isinstance(error, Forbidden):
        await ctx.reply('Error: I do not have permissions to do that command.')
    else:
        #for debugging purposes
        print(error)

@termino.event
async def on_member_join(member: discord.Member):
    data = get_server_data('data.json')
    welcome_channel = termino.get_channel(data[str(member.guild.id)]['join_announcement_channel'])
    welcome_embed = discord.Embed(title = f'Looks like someone joined the server!', description = f'Welcome {member.mention}!', color = discord.Colour.green())
    welcome_embed.add_field(name = 'Number of members:', value = f'`Total: {len(member.guild.members)}`\n`Not including bots: {len([member for member in member.guild.members if not member.bot])}`')
    welcome_embed.set_thumbnail(url = member.avatar_url)

    if data[str(member.guild.id)]['join_role'] != None:
        await member.add_roles(member.guild.get_role(data[str(member.guild.id)]['join_role']))

    if data[str(member.guild.id)]['join_announcement_channel'] != None:
        welcome_channel = termino.get_channel(data[str(member.guild.id)]['join_announcement_channel'])
        await welcome_channel.send(embed = welcome_embed)

    if data[str(member.guild.id)]['welcome_dm'] != None:
        await member.send(data[str(member.guild.id)]['welcome_dm'])

@termino.command()
async def initialize(ctx):
    data = get_server_data('data.json')
    if str(ctx.guild.id) in data:
        await ctx.reply('Bot already initialized')
    else:
        data[str(ctx.guild.id)] = {"mute_role":None, "join_announcement_channel": None, "join_role": None, "welcome_dm": None}
        change_server_data('data.json',data)
        await ctx.send(f'Bot initialized in {ctx.guild} discord server.')

@termino.command()
async def help(ctx, cmd_category = None):
    if cmd_category == None:
        embd = discord.Embed(title = 'Need help? Refer down below!',
                description = 'Check out the commands!')
        embd.add_field(name = ':basketball: For fun :basketball: :', value = '`$help fun`',  inline = False)
        embd.add_field(name = ':shield: For moderation :shield: :',value = '`$help moderation`', inline = True)
        await ctx.reply(embed = embd)
    elif cmd_category == 'fun':
        embd = discord.Embed(title = 'These are the commands for fun!')
        embd.add_field(name = 'Here:', value = get_help_fun(), inline = False)
        embd.set_footer(text = 'Hope you have fun lmfao')
        await ctx.reply(embed = embd)
    elif cmd_category == 'moderation':
        embd = discord.Embed(title = 'These are the commands for discord mods to use!')
        embd.add_field(name = 'Here:', value = get_help_mod(), inline = False)
        embd.set_footer(text = 'Still in development!')
        await ctx.reply(embed = embd)
    else:
        await ctx.reply('Command category does not exist bro.')

fun.add_command(termino)
moderation.add_command(termino)

termino.run(get_token())

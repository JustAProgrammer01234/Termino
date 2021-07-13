import discord
from discord import Forbidden
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingPermissions, NoPrivateMessage

intents = discord.Intents.all()
termino = commands.Bot(command_prefix = '$', help_command = None, intents = intents, activity = discord.Game(name = 'for $help'))

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} is ready to go.')
        print('-----------------------------------')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.reply("Well, couldn't find that command. Try typing $help so you would see the commands.")
        elif isinstance(error, Forbidden):
            await ctx.reply('I do not have permissions to do that command.')
        elif isinstance(error, NoPrivateMessage):
            await ctx.reply('That command cannot be used in dm.')
        else:
            #for debugging purposes
            print(error)

def setup(bot):
    bot.add_cog(Main(bot))
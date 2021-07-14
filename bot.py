import os
import discord
from discord import Forbidden
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingPermissions, NoPrivateMessage

class TerminoHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        await self.context.send("This is help")
       
    async def send_command_help(self, command):
        await self.context.send("This is help command")
      
    async def send_group_help(self, group):
        await self.context.send("This is help group")
    
    async def send_cog_help(self, cog):
        await self.context.send("This is help cog")

class Bot(commands.Bot):
    def __init__(self):      
        for cog in os.listdir('./cogs'):
            if os.path.isfile(cog):
                self.load_extension(cog)

        super().__init__(command_prefix = '$',
        help_command = TerminoHelp(),
        intents = discord.Intents.all(),
        activity = discord.Game(name = 'for $help'))


        
termino = Bot()
termino.run(os.environ['BOT_TOKEN'])
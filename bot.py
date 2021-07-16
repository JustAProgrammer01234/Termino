import os
import discord
from discord import Forbidden
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, NoPrivateMessage

class TerminoHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        destination = self.get_destination()
        help_embed = discord.Embed(title = 'See the commands Termino has down below by exploring each category!',
        description = '**Tip:** For more details about a command, type `$help <command>`.',
        colour = discord.Colour.green())
        index_count = 0

        for category in mapping:
            if category != None:
                if index_count % 3 == 0:
                    help_embed.add_field(name = f'{category.qualified_name}', value = f'`$help {category.qualified_name}`', inline = False)
                else:
                    help_embed.add_field(name = f'{category.qualified_name}', value = f'`$help {category.qualified_name}`', inline = True)
            index_count += 1

        await destination.send(embed = help_embed)

    async def send_cog_help(self, cog):
        destination = self.get_destination()
        commands = cog.get_commands()
        command_list = ''
        help_embed = discord.Embed(title = f'Info about category: {cog.qualified_name}', description = f'{cog.description}', colour = discord.Colour.blue())

        for i in range(len(commands)):
            command_list += f'**{i + 1}.** `{commands[i]}`\n'

        help_embed.add_field(name = 'Commands:', value = command_list)
        help_embed.set_footer(text = "Don't forget to put $ before each command!")
        await destination.send(embed = help_embed)

    async def send_command_help(self, command):
        destination = self.get_destination()
        help_embed = discord.Embed(title = f'Help for command: {command.name}', description = command.help, color = discord.Colour.red())

        if len(command.aliases) > 0: 
            help_embed.add_field(name = '__**Aliases**__', value = f"{'**,**'.join([f'`{a}`' for a in command.aliases])}", inline = False)
        else:
            help_embed.add_field(name = '__**Aliases**__', value = f'No aliases are found in this command.', inline = False)
        
        help_embed.add_field(name = '__**Syntax**__', value = f'`{self.get_command_signature(command)}`', inline = False)
        await destination.send(embed = help_embed)
      
    async def send_group_help(self, group):
        destination = self.get_destination()
        await destination.send('This is help group.')

    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            error_embed = discord.Embed(title = ':warning: Whoops! An error occurred! :warning:')
            error_embed.description = error,
            error_embed.colour = discord.Colour.red()
            await ctx.send(embed = error_embed)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = '$',
        intents = discord.Intents.all(),
        activity = discord.Game(name = 'for $help'),
        help_command = TerminoHelp()
        )

termino = Bot()

@termino.listen()
async def on_ready():
    print(f"{termino.user.name} is now ready to go.")

@termino.listen()
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.reply("Looks like I couldn't find that command. Try typing $help so you will know all the lists of commands I have.")
    elif isinstance(error, NoPrivateMessage):
        await ctx.reply("That command cannot be used in dm.")
    else:
        print(error)

if __name__ == '__main__':
    for cog in os.listdir('./cogs'):
        if cog.endswith('.py') and cog != '__init__.py':
            termino.load_extension(f'cogs.{cog[:-3]}')

    termino.run(os.getenv('BOT_TOKEN'))
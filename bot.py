import os
import discord
from discord import Forbidden
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, NoPrivateMessage

class TerminoHelp(commands.HelpCommand):

    async def send_bot_help(self, mapping):
        destination = self.get_destination()

        tip_embed = discord.Embed(title = 'Tip:', description = 'Type `$help <command>` for more details about a command.', colour = 0xFFFF)
        help_embed = discord.Embed(title = 'Termino help.', description = 'See the commands Termino has down below by exploring each category!', colour = 0xFFFF)
        help_embed.set_author(name = f"Help provided by: {self.context.me.name}#{self.context.me.discriminator}", icon_url = self.context.me.avatar_url)
        help_embed.set_footer(text = f"Requested by: {self.context.author.name}#{self.context.author.discriminator}", icon_url = self.context.author.avatar_url)
        help_embed.set_thumbnail(url = self.context.me.avatar_url)

        for category in mapping:
            if category != None:
                help_embed.add_field(name = f'{category.qualified_name.title()}', value = f'`$help {category.qualified_name}`', inline = True)

        await destination.send(embed = tip_embed)
        await destination.send(embed = help_embed)

    async def send_cog_help(self, cog):
        destination = self.get_destination()
        commands = cog.get_commands()
        command_list = ''

        note_embed = discord.Embed(title = 'Note:', description = "Don't forget to add `$` before you type a command.", color = 0xFFFF)
        help_embed = discord.Embed(title = f'Info about category: {cog.qualified_name.title()}', description = f'{cog.description}', color = 0xFFFF)
        help_embed.set_author(name = f"Help provided by: {self.context.me.name}#{self.context.me.discriminator}", icon_url = self.context.me.avatar_url)
        help_embed.set_footer(text = f"Requested by: {self.context.author.name}#{self.context.author.discriminator}", icon_url = self.context.author.avatar_url)
        help_embed.set_thumbnail(url = self.context.me.avatar_url)

        for i in range(len(commands)):
            command_list += f'**{i + 1}.** `{commands[i]}`\n'

        help_embed.add_field(name = 'Commands:', value = command_list)
        await destination.send(embed = note_embed)
        await destination.send(embed = help_embed)

    async def send_command_help(self, command):
        destination = self.get_destination()
        help_embed = discord.Embed(title = f'Help for command: {command.name}', color = 0xFFFF)
        help_embed.set_author(name = f"Help provided by: {self.context.me.name}#{self.context.me.discriminator}", icon_url = self.context.me.avatar_url)
        help_embed.set_footer(text = f"Requested by: {self.context.author.name}#{self.context.author.discriminator}", icon_url = self.context.author.avatar_url)
        help_embed.set_thumbnail(url = self.context.me.avatar_url)
        help_embed.add_field(name = "Description:", value = command.help, inline = False)

        if len(command.aliases) > 0: 
            help_embed.add_field(name = 'Aliases:', value = f"{'**,**'.join([f'`{a}`' for a in command.aliases])}", inline = False)
        else:
            help_embed.add_field(name = 'Aliases:', value = f'No aliases are found in this command.', inline = False)
        
        help_embed.add_field(name = 'Syntax:', value = f'`{self.get_command_signature(command)}`', inline = False)
        await destination.send(embed = help_embed)

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix = '$',
        intents = discord.Intents.all(),
        activity = discord.Game(name = 'for $help'),
        help_command = TerminoHelp(),
        description = 'Just your average bot.',
        owner_id = 790767157523775518
        )

termino = Bot()

@termino.event
async def on_ready():
    print(f"{termino.user.name} is now ready to go.")

@termino.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        cmd_not_found_embed = discord.Embed(title = "Looks like I coudn't find that command.", description = 'Try typing `$help`', color = discord.Colour.red())
        await ctx.send(embed = cmd_not_found_embed)
    elif not hasattr(error, 'original'):
        command_error_embed = discord.Embed(title = "Whoops! An error occured...", 
        description = f'```{error}```',
        color = discord.Colour.red())
        await ctx.send(embed = command_error_embed)
        
if __name__ == '__main__':
    for cog in os.listdir('./cogs'):
        if cog.endswith('.py') and cog != '__init__.py':
            termino.load_extension(f'cogs.{cog[:-3]}')

    termino.run(os.getenv('BOT_TOKEN'))
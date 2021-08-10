import discord 
from discord.ext import commands 

class TerminoHelp(commands.HelpCommand):

    async def send_bot_help(self, mapping):
        ctx = self.context
        description = '''
        Type `$help <command>` for more info about a command.
        ''' 

        help_embed = discord.Embed(title = f'{ctx.me.name} help.', description = description, colour = 0xFFFF)
        help_embed.set_author(name = f"Help provided by: {ctx.me}", icon_url = ctx.me.avatar_url)
        help_embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.context.author.avatar_url)
        help_embed.set_thumbnail(url = ctx.me.avatar_url)

        for category in mapping:
            if category != None:
                help_embed.add_field(name = f'{category}', value = f'`$help {category.qualified_name}`', inline = True)

        await ctx.reply(embed = help_embed)

    async def send_cog_help(self, cog):
        ctx = self.context
        commands = cog.get_commands()
        command_list = ''

        help_embed = discord.Embed(title = f'Info about category: {cog}', description = f'{cog.description}', color = 0xFFFF)
        help_embed.set_author(name = f"Help provided by: {ctx.me}", icon_url = ctx.me.avatar_url)
        help_embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = ctx.author.avatar_url)
        help_embed.set_thumbnail(url = ctx.me.avatar_url)

        for i in range(len(commands)):
            command_list += f'> **{i + 1}.** `{commands[i]}`\n'

        help_embed.add_field(name = 'Commands:', value = command_list)
        await ctx.reply(embed = help_embed)

    async def send_command_help(self, command):
        ctx = self.context

        help_embed = discord.Embed(title = f'Help for command: {command.name}', color = 0xFFFF)
        help_embed.set_author(name = f"Help provided by: {ctx.me}", icon_url = ctx.me.avatar_url)
        help_embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.context.author.avatar_url)
        help_embed.set_thumbnail(url = ctx.me.avatar_url)
        help_embed.add_field(name = "Description:", value = command.help, inline = False)

        if len(command.aliases) > 0: 
            help_embed.add_field(name = 'Aliases:', value = f"{'**,**'.join([f'`{a}`' for a in command.aliases])}", inline = False)
        else:
            help_embed.add_field(name = 'Aliases:', value = f'No aliases are found in this command.', inline = False)
        
        help_embed.add_field(name = 'Syntax:', value = f'`{self.get_command_signature(command)}`', inline = False)
        await ctx.reply(embed = help_embed)
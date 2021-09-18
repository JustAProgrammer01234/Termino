import discord 
import inspect
from discord.ext import commands 

class CategorySelect(discord.ui.Select):
    def __init__(self, bot, mapping):
        self.bot = bot 
        categories = []
        for category in mapping:
            if category is not None:
                categories.append(discord.SelectOption(
                    label = category.qualified_name.title(), 
                    description = category.description)
                )

        super().__init__(placeholder = 'Select a category.', min_values = 1, max_values = 1, options = categories)

    async def callback(self, interaction: discord.Interaction):
        cog = self.bot.get_cog(self.values[0])
        commands = cog.get_commands()
        command_list = ''
        me = interaction.guild.me
        author = interaction.user

        for i in range(len(commands)):
            command_list += f'> **{i + 1}.** `{commands[i]}`\n'

        help_embed = discord.Embed(title=cog, description=f'{cog.description}', timestamp=discord.utils.utcnow())
        help_embed.set_author(name = f"Help provided by: {me}", icon_url=me.avatar.url)
        help_embed.set_footer(text = f"Requested by: {author}", icon_url=author.avatar.url)
        help_embed.add_field(name = 'Commands:', value=command_list)

        await interaction.response.edit_message(embed=help_embed)

class SourceButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            style = discord.ButtonStyle.gray,
            label = 'Source',
            url = 'https://github.com/JustAProgrammer01234/Termino'
        )

class HelpView(discord.ui.View):
    def __init__(self, bot, mapping):
        super().__init__()
        self.add_item(CategorySelect(bot, mapping))

class TerminoHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        ctx = self.context
        description = inspect.cleandoc(
            f'''
            Hello fellow discord users!
            My name is {ctx.me.name} and I'm a discord bot used for many things!
            You can see the categories I have down below:
            '''
        ) 

        help_embed = discord.Embed(title=f'{ctx.me.name} help', description=description, timestamp=discord.utils.utcnow())
        help_embed.set_author(name = f"Help provided by: {ctx.me}", icon_url = ctx.me.avatar.url)
        help_embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.context.author.avatar.url)
        help_embed.set_thumbnail(url = ctx.me.avatar.url)

        for category in mapping:
            if category is not None:
                help_embed.add_field(name = str(category), value = f'**`{category.description}`**', inline = False)

        view = HelpView(ctx.bot, mapping)
        view.add_item(SourceButton())
        await ctx.reply(embed = help_embed, view = view)

    async def send_cog_help(self, cog):
        ctx = self.context
        commands = cog.get_commands()
        command_list = ''

        for i in range(len(commands)):
            command_list += f'> **{i + 1}.** `{commands[i]}`\n'

        help_embed = discord.Embed(title = cog, description = f'{cog.description}')
        help_embed.set_author(name = f"Help provided by: {ctx.me}", icon_url = ctx.me.avatar_url)
        help_embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = ctx.author.avatar_url)
        help_embed.set_thumbnail(url = ctx.me.avatar_url)
        help_embed.add_field(name = 'Commands:', value = command_list)

        view = HelpView(ctx.bot, self.get_bot_mapping())
        await ctx.reply(embed = help_embed, view=view)
 
    async def send_command_help(self, command):
        ctx = self.context

        help_embed = discord.Embed(title = f'Help for command: {command.name}')
        help_embed.set_author(name = f"Help provided by: {ctx.me}", icon_url = ctx.me.avatar_url)
        help_embed.set_thumbnail(url = ctx.me.avatar_url)
        help_embed.add_field(name = "Description:", value = command.help, inline = False)
        help_embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.context.author.avatar_url)

        if len(command.aliases) > 0: 
            help_embed.add_field(name = 'Aliases:', value = f"{'**,**'.join([f'`{a}`' for a in command.aliases])}", inline = False)
        else:
            help_embed.add_field(name = 'Aliases:', value = f'No aliases are found in this command.', inline = False)
        
        help_embed.add_field(name = 'Syntax:', value = f'`{self.get_command_signature(command)}`', inline = False)

        view = HelpView(ctx.bot, self.get_bot_mapping())
        await ctx.reply(embed = help_embed, view=view)

    async def send_group_help(self, group):
        ctx = self.context
        sub_command_list = list(group.commands)
        sub_commands = ''

        for i in range(len(sub_command_list)):
            command_signature = self.get_command_signature(sub_command_list[i])
            sub_commands += f'> **{i + 1}.** {command_signature}\n'

        help_embed = discord.Embed(title = f'Help for command group: {group.qualified_name}', description = group.short_doc, color = 0xFFFF)
        help_embed.set_author(name = f"Help provided by: {ctx.me}", icon_url = ctx.me.avatar_url)
        help_embed.set_thumbnail(url = ctx.me.avatar_url)
        help_embed.add_field(name = 'Sub commands:', value = sub_commands)
        help_embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.context.author.avatar_url)

        view = HelpView(ctx.bot, self.get_bot_mapping())
        await ctx.reply(embed = help_embed, view=view)
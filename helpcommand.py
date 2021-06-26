import discord 
from discord.ext import commands 
from noncoroutines import get_help_fun, get_help_mod, get_help_util_welcome, get_help_util_mute, get_help_game, get_json_data

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.command_details = get_json_data('helpcommand.json')

    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        embd = discord.Embed(title = 'Need help? Refer down below to see the commands!',
                description = '**Tip:**\n Type $help then a command for more details about it like this\n `$help <command>`',
                color = discord.Colour.green())
        embd.add_field(name = ':basketball: For fun :basketball:', value = '`$help fun`',  inline = False)
        embd.add_field(name = ':shield: For moderation :shield:',value = '`$help mod`', inline = False)
        embd.add_field(name = ':gear: For settings :gear:',value = '`$help settings`', inline = False)
        embd.add_field(name = ':video_game: Games :video_game:', value = '`$help games`', inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def fun(self, ctx):
        embd = discord.Embed(title = 'These are the commands for fun!', description = get_help_fun(), color = discord.Colour.green())
        await ctx.send(embed = embd)

    @help.command()
    async def mod(self, ctx):
        embd = discord.Embed(title = 'Moderator commands!', description = get_help_mod(), color = discord.Colour.green())
        embd.set_footer(text = "Don't forget to sync my perms for them to work!")
        await ctx.send(embed = embd)

    @help.command()
    async def settings(self, ctx):
        embd = discord.Embed(title = 'Termino utilities!', color = discord.Colour.green())
        embd.add_field(name = 'Welcomes:', value = get_help_util_welcome(), inline = False)
        embd.add_field(name = 'Mute command setup:', value = get_help_util_mute(), inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def games(self, ctx):
        embd = discord.Embed(title = 'Games!', description = get_help_game(), color = discord.Colour.green())
        await ctx.send(embed = embd)

    @help.command()
    async def display(self, ctx):
        embd = discord.Embed(title = 'Command: display', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['display']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['display']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def randomnum(self, ctx):
        embd = discord.Embed(title = 'Command: randomnum', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['randomnum']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['randomnum']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def solve(self, ctx):
        embd = discord.Embed(title = 'Command: solve', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['solve']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['solve']['aliases'], inline = False)
        await ctx.send(embed = embd) 

    @help.command()
    async def randomslap(self, ctx):
        embd = discord.Embed(title = 'Command: randomslap', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['randomslap']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['randomslap']['aliases'], inline = False)
        await ctx.send(embed = embd) 

    @help.command(name = '8ball')
    async def _8ball(self, ctx):
        embd = discord.Embed(title = 'Command: 8ball', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['8ball']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['8ball']['aliases'], inline = False)
        await ctx.send(embed = embd) 

    @help.command()
    async def iseven(self, ctx):
        embd = discord.Embed(title = 'Command: iseven', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['iseven']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['iseven']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def slap(self, ctx):
        embd = discord.Embed(title = 'Command: slap', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['slap']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['slap']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def hack(self, ctx):
        embd = discord.Embed(title = 'Command: hack', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['hack']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['hack']['aliases'], inline = False)
        await ctx.send(embed = embd) 

    @help.command()
    async def kick(self, ctx):
        embd = discord.Embed(title = 'Command: kick', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['kick']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['kick']['aliases'], inline = False)
        await ctx.send(embed = embd) 

    @help.command()
    async def ban(self, ctx):
        embd = discord.Embed(title = 'Command: ban', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['ban']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['ban']['aliases'], inline = False)
        await ctx.send(embed = embd) 

    @help.command()
    async def unban(self, ctx):
        embd = discord.Embed(title = 'Command: unban', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['unban']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['unban']['aliases'], inline = False)
        await ctx.send(embed = embd) 

    @help.command()
    async def mute(self, ctx):
        embd = discord.Embed(title = 'Command: mute', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['mute']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['mute']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def banlist(self, ctx):
        embd = discord.Embed(title = 'Command: banlist', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['banlist']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['banlist']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command(name = 'set-join-role')
    async def set_join_role(self, ctx):
        embd = discord.Embed(title = 'Command: set-join-role', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['set-join-role']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['set-join-role']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command(name = 'set-join-channel')
    async def set_join_channel(self, ctx):
        embd = discord.Embed(title = 'Command: set-join-channel', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['set-join-channel']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['set-join-channel']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command(name = 'welcome-dm-message')
    async def set_dm_message(self, ctx):
        embd = discord.Embed(title = 'Command: welcome-dm-message', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['welcome-dm-message']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['welcome-dm-message']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command(name = 'add-mute-role')
    async def add_mute_role(self, ctx):
        embd = discord.Embed(title = 'Command: add-mute-role', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['add-mute-role']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['add-mute-role']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command(name = 'remove-mute-role')
    async def remove_mute_role(self, ctx):
        embd = discord.Embed(title = 'Command: remove-mute-role',
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['remove-mute-role']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['remove-mute-role']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command(aliases = ['rock-paper-scissors'])
    async def rock_paper_scissors(self, ctx):
        embd = discord.Embed(title = 'Command: rock-paper-scissors', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['rock-paper-scissors']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['rock-paper-scissors']['aliases'], inline = False)
        await ctx.send(embed = embd)

    @help.command()
    async def dice(self, ctx):
        embd = discord.Embed(title = 'Command: dice', 
                            colour = discord.Colour.green()
                            )
        embd.add_field(name = 'Description:', value = self.command_details['dice']['description'], inline = False)
        embd.add_field(name = 'Aliases:', value = self.command_details['dice']['aliases'], inline = False)
        await ctx.send(embed = embd)

def setup(bot):
    bot.add_cog(Help(bot))

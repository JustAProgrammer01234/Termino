import os
import dotenv
import discord
from cogs.util import db, reddit
from discord.ext import commands
from terminohelp import TerminoHelp

class Bot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix = ['$','termino '],
            intents = discord.Intents.all(),
            activity = discord.Game(name = 'for $help'),
            help_command = TerminoHelp(),
            description = 'Just your average bot.',
            owner_id = 790767157523775518
        )

    async def on_connect(self):
        print(f'{termino.user} successfully connected to discord.')

        for cog in os.listdir('./cogs'):
            if cog.endswith('.py') and cog != '__init__.py':
                self.load_extension(f'cogs.{cog[:-3]}')

        self.database = db.TerminoDb(os.getenv('PSQL_USER'), os.getenv('PSQL_PASSWD'), os.getenv('PSQL_HOST'), os.getenv('PSQL_PORT'), os.getenv('PSQL_DB'))
        self.reddit = reddit.SubReddit(client_id = os.getenv('REDDIT_CLIENT_ID'), client_secret = os.getenv('REDDIT_CLIENT_SECRET'), user_agent = os.getenv('REDDIT_USER_AGENT'))

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            cmd_not_found_embed = discord.Embed(title = "Looks like I coudn't find that command.", description = 'Try typing `$help`', color = discord.Colour.red())
            await ctx.send(embed = cmd_not_found_embed)

        elif not hasattr(error, 'original') and not isinstance(error, commands.MissingPermissions):
            command_error_embed = discord.Embed(title = "Whoops! An error occured...", 
                                                description = f'```python\n{error}```',
                                                color = discord.Colour.red())
            await ctx.send(embed = command_error_embed)
        
        else:
            print(error)
        
if __name__ == '__main__':
    dotenv.load_dotenv()
    termino = Bot()
    termino.run(os.getenv('BOT_TOKEN'))
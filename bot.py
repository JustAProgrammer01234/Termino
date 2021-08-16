import os
import discord
import asyncpg
from cogs.util import reddit
from discord.ext import commands
from cogs.util.database import termino_servers
from terminohelp import TerminoHelp

class Bot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix = '$.',
            intents = discord.Intents.all(),
            activity = discord.Game(name = 'for $.help'),
            help_command = TerminoHelp(),
            description = 'Just your average bot.',
            owner_id = 790767157523775518
        )
        self.reddit = reddit.SubReddit(client_id = os.getenv('REDDIT_CLIENT_ID'), client_secret = os.getenv('REDDIT_CLIENT_SECRET'), user_agent = os.getenv('REDDIT_USER_AGENT'))

    async def on_connect(self):
        print(f'{termino.user} successfully connected to discord.')
    
        user = os.getenv('PSQL_USER')
        passwd = os.getenv('PSQL_PASSWD')
        host = os.getenv('PSQL_HOST')
        port = os.getenv('PSQL_PORT')
        database = os.getenv('PSQL_DB')

        for cog in os.listdir('./cogs'):
            if cog.endswith('.py') and cog != '__init__.py':
                self.load_extension(f'cogs.{cog[:-3]}')

        async with asyncpg.create_pool(dsn = f'postgres://{user}:{passwd}@{host}:{port}/{database}') as pool:
            self.pool = pool

        self.servers_db = termino_servers.TerminoServers(self)
        await self.servers_db.create_table()

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

    async def on_guild_join(self, guild):
        await self.servers_db.initialize_server(guild.id)
        
if __name__ == '__main__':
    termino = Bot()
    termino.run(os.getenv('BOT_TOKEN'))
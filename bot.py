import os
import discord
import asyncpg
import asyncio
import wavelink
from cogs.util import reddit
from discord.ext import commands
from cogs.util.database import termino_servers
from terminohelp import TerminoHelp

async def get_prefix(bot, message):
    if not message.guild:
        return '$.'
    server_prefix = await bot.servers_db.fetch_server_info(message.guild.id)
    return server_prefix['prefix']

class Bot(commands.AutoShardedBot):
    def __init__(self):

        user = os.getenv('PSQL_USER')
        passwd = os.getenv('PSQL_PASSWD')
        database = os.getenv('PSQL_DB')

        self.pool = asyncpg.create_pool(dsn = f'postgres://{user}:{passwd}@172.18.0.2:5432/{database}')
        self.servers_db = termino_servers.TerminoServers(self.pool)
       
        super().__init__(
            command_prefix = get_prefix,
            intents = discord.Intents.all(),
            activity = discord.Game(name = 'for $.help'),
            help_command = TerminoHelp(),
            description = 'Just your average bot.',
            owner_id = 790767157523775518
        )

        self.loop = asyncio.get_event_loop()
        self.loop.create_task(
            self.create_wavelink_client()
        )
        self.create_reddit_client()
        self.load_cogs()

    async def on_connect(self):
        print(f'{self.user} successfully connected to Discord.')

    async def on_ready(self):
        print(f'{self.user} is ready.')

    async def on_command_error(self, ctx, error):
        error_embed = discord.Embed(
            color = discord.Colour.red()
        )

        await ctx.message.add_reaction('\U0000274c')
        
        if isinstance(error, commands.CommandNotFound):
            error_embed.title = "Looks like I couldn't find that command."
            error_embed.description = f"Try typing `{self.command_prefix}help`."

        elif not hasattr(error, 'original') and not isinstance(error, commands.MissingPermissions):
            error_embed.title = "Whoops! An error occured..."
            error_embed.description = f"```python\n{error}```"

        elif isinstance(error, commands.MissingPermissions):
            error_embed.title = ':no_entry: Permission denied! :no_entry:'
            error_embed.description = 'Or you may be affected by hierarchy.'
        
        elif hasattr(error, 'original'):
            if isinstance(error.original, discord.Forbidden):
                error_embed.title = ':warning: Bot has missing perms! :warning:'
                error_embed.description = 'Or the bot may be affected by hierarchy.'

        await ctx.send(embed = error_embed)

    async def on_guild_join(self, guild):
        await self.servers_db.initialize_row(guild.id)

    async def on_guild_remove(self, guild):
        await self.servers_db.delete_row(guild.id)

    def load_cogs(self):
        for cog in os.listdir('./cogs'):
            if cog.endswith('.py') and cog != '__init__.py':
                try:
                    self.load_extension(f'cogs.{cog[:-3]}')
                except:
                    pass

    async def create_wavelink_client(self):
        self.wavelink = wavelink.Client(bot = self)
        await self.wavelink.initiate_node(
                host = '172.18.0.2',
                port = 2333,
                password = os.getenv('LAVALINK_PASSWD'),
                identifier = 'node_identifier',
                rest_uri = 'http://172.18.0.2:2333',
                region = 'us_central'
            )

    def create_reddit_client(self):
        self.reddit = reddit.SubReddit(
            client_id = os.getenv('REDDIT_CLIENT_ID'), 
            client_secret = os.getenv('REDDIT_CLIENT_SECRET')
        )

    @classmethod
    async def main(cls):
        termino = cls()

        try:
            await termino.servers_db.create_table()
            await termino.start(os.getenv('BOT_TOKEN'))

        except Exception as e:
            print(f'An exception occured: {e}')
            await termino.start(os.getenv('BOT_TOKEN'))

        finally:
            await termino.pool.close()
            await termino.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Bot.main())
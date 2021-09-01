import os
import discord
import asyncpg
import asyncio
import wavelink
from cogs.util import reddit
from discord.ext import commands
from cogs.util.database import termino_servers
from terminohelp import TerminoHelp

user = os.getenv('PSQL_USER')
passwd = os.getenv('PSQL_PASSWD')
database = os.getenv('PSQL_DB')

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix = '$.',
            intents = discord.Intents.all(),
            activity = discord.Game(name = 'for $.help'),
            help_command = TerminoHelp(),
            description = 'Just your average bot.',
            owner_id = 790767157523775518
        )
        self.loop = asyncio.get_event_loop()

        self.wavelink = wavelink.Client(bot = self)
        self.loop.create_task(self.start_wavelink_nodes())
        self.create_reddit_client()

        self.load_cogs()

    def load_cogs(self):
        for cog in os.listdir('./cogs'):
            if cog.endswith('.py') and cog != '__init__.py':
                try:
                    self.load_extension(f'cogs.{cog[:-3]}')
                except:
                    pass

    async def start_wavelink_nodes(self):
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

    async def on_connect(self):
        print(f'{self.user} successfully connected to Discord.')

    async def on_ready(self):
        print(f'{self.user} is ready.')

    async def on_message(self, message):
        if message.content == f'<@{self.user.id}>':
            await message.channel.send(f'My prefix is `{self.command_prefix}`.')
        await self.process_commands(message)

    async def on_command_error(self, ctx, error):
        error_embed = discord.Embed(color = discord.Colour.red())

        if not isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction('\U0000274c')

        if not hasattr(error, 'original') and not isinstance(error, commands.MissingPermissions):
            error_embed.title = "Whoops! An error occured..."
            error_embed.description = f"```python\n{error}```"

        elif isinstance(error, commands.MissingPermissions):
            error_embed.title = ':no_entry: Permission denied! :no_entry:'
            error_embed.description = 'Or you may be affected by hierarchy.'
        
        elif hasattr(error, 'original'):
            if isinstance(error.original, discord.Forbidden):
                error_embed.title = ':warning: Bot has missing perms! :warning:'
                error_embed.description = 'Or the bot may be affected by hierarchy.'

        try:
            await ctx.send(embed = error_embed)
        except:
            pass 

    async def on_guild_join(self, guild):
        await self.servers_db.initialize_row(guild.id)

    async def on_guild_remove(self, guild):
        await self.servers_db.delete_row(guild.id)

    @classmethod
    async def main(cls):
        async with asyncpg.create_pool(f'postgres://{user}:{passwd}@172.18.0.2:5432/{database}') as pool:
            termino = cls()
            termino.servers_db = termino_servers.TerminoServers(pool)
            await termino.servers_db.create_table()
            await termino.start(os.getenv('BOT_TOKEN'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Bot.main())
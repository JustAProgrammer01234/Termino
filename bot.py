import os
import re 
import discord
import asyncpg
import asyncio
import wavelink
from discord.ext import commands
from cogs.util.clients import db
from terminohelp import TerminoHelp
from cogs.util.clients import reddit

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

    def load_cogs(self):
        for cog in os.listdir('./cogs'):
            if cog.endswith('.py') and cog != '__init__.py':
                try:
                    self.load_extension(f'cogs.{cog[:-3]}')
                except Exception as e:
                    print(f'Error loading cog {cog}: {e}')

    async def on_connect(self):
        print(f'{self.user} successfully connected to Discord.')

    async def on_ready(self):
        print(f'{self.user} is ready.')

    async def on_message(self, message):
        mentioned = discord.utils.find(lambda m: m.id == self.user.id, message.mentions)

        if message.author == self.user:
            return 

        if mentioned:
            await message.channel.send(f'My prefix is `{self.command_prefix}`.')
        await self.process_commands(message)

    async def on_command_error(self, ctx, error):
        error_embed = discord.Embed(color = discord.Colour.red())

        if not isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction('\U0000274c')

        if not hasattr(error, 'original') and not isinstance(error, commands.MissingPermissions) and not isinstance(error, commands.CommandNotFound):
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

        print(error)

async def start_wavelink_nodes(lavalink_host, lavalink_passwd, bot):
    await bot.wavelink.initiate_node(
        host = lavalink_host,
        port = 2333,
        password = lavalink_passwd,
        identifier = 'node_identifier',
        rest_uri = f'http://{lavalink_host}:2333',
        region = 'us_central'
    )

async def main():

    token = os.getenv('BOT_TOKEN')

    psql_user = os.getenv('PSQL_USER')
    psql_passwd = os.getenv('PSQL_PASSWD')
    psql_host = os.getenv('PSQL_HOST')
    psql_db = os.getenv('PSQL_DB')

    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')

    lavalink_host = os.getenv('LAVALINK_HOST')
    lavalink_passwd = os.getenv('LAVALINK_PASSWD')

    termino = Bot()
    termino.loop = asyncio.get_event_loop()

    try:
        pool = await asyncpg.create_pool(dsn=f'postgres://{psql_user}:{psql_passwd}@{psql_host}:5432/{psql_db}')
        termino.db = await db.DbClient(pool)
        termino.loop.create_task(start_wavelink_nodes(lavalink_host, lavalink_passwd, termino))
        termino.reddit = reddit.RedditClient(client_id=client_id, client_secret=client_secret)
    except Exception as e:
        print(f'An exception occured while initializing the api clients: {e}')

    termino.load_cogs()

    try:
        print("Starting the damn bot.")
        await termino.start(token)
    except KeyboardInterrupt:
        print("Okay, I'll stop.")
        await termino.close()

if __name__ == '__main__':
    try:
        print('Trying to run the whole script.')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('Aborting...')
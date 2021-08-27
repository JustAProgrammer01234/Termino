import os
import discord
import asyncpg
import asyncio
from cogs.util import reddit
from discord.ext import commands
from cogs.util.database import termino_servers
from terminohelp import TerminoHelp

async def get_prefix(bot, message):
    if not message.guild:
        return '$'
    server_prefix = await bot.servers_db.fetch_server_info(message.guild.id)['prefix']
    return server_prefix

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix = get_prefix,
            intents = discord.Intents.all(),
            activity = discord.Game(name = 'for $.help'),
            help_command = TerminoHelp(),
            description = 'Just your average bot.',
            owner_id = 790767157523775518
        )
        self.reddit = reddit.SubReddit(client_id = os.getenv('REDDIT_CLIENT_ID'), 
                            client_secret = os.getenv('REDDIT_CLIENT_SECRET'), 
                            user_agent = os.getenv('REDDIT_USER_AGENT')
                        )

    async def on_connect(self):
        print(f'{self.user} successfully connected to discord.')
    
        for cog in os.listdir('./cogs'):
            if cog.endswith('.py') and cog != '__init__.py':
                try:
                    self.load_extension(f'cogs.{cog[:-3]}')
                except:
                    pass

    async def on_command_error(self, ctx, error):
        error_embed = discord.Embed(
            color = discord.Colour.red()
        )

        await ctx.message.add_reaction('\U0000274c')
        
        if isinstance(error, commands.CommandNotFound):
            error_embed.title = "Looks like I couldn't find that command."
            error_embed.description = f"Try typing `{self.command_prefix}help`"
            await ctx.send(embed = error_embed)

        elif not hasattr(error, 'original') and not isinstance(error, commands.MissingPermissions):
            error_embed.title = "Whoops! An error occured..."
            error_embed.description = f"```python\n{error}```"
            await ctx.send(embed = error_embed)
        
        else:
            print(error)

    async def on_guild_join(self, guild):
        await self.servers_db.initialize_server(guild.id)

    async def on_guild_remove(self, guild):
        await self.servers_db.delete_row(guild.id)

async def main():
    termino = Bot()

    user = os.getenv('PSQL_USER')
    passwd = os.getenv('PSQL_PASSWD')
    host = os.getenv('PSQL_HOST')
    port = os.getenv('PSQL_PORT')
    database = os.getenv('PSQL_DB')

    try:
        async with asyncpg.create_pool(dsn = f'postgres://{user}:{passwd}@{host}:{port}/{database}') as pool:
            termino.pool = pool
            termino.servers_db = termino_servers.TerminoServers(termino)

            await termino.servers_db.create_table()
            await termino.start(os.getenv('BOT_TOKEN'))
    except:
        await termino.start(os.getenv('BOT_TOKEN'))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
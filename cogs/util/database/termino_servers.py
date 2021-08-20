import asyncpg

class TerminoServers:

    def __init__(self, bot):
        self.bot = bot

    async def create_table(self):
        try:
            async with self.bot.pool.acquire() as con:
                await con.execute('''
                CREATE TABLE termino_servers (
                    guild_id    BIGINT,
                    welcome_channel_id  BIGINT,
                    welcome_role_id BIGINT,
                    welcome_dm  TEXT,
                    mute_role_id    BIGINT,
                    prefix  TEXT
                );
                ''')
        except asyncpg.exceptions.DuplicateTableError:
            pass

    async def initialize_server(self, guild_id):
        async with self.bot.pool.acquire() as con:
            await con.execute('''
            INSERT INTO termino_servers VALUES ($1, $2, $3, $4, $5, $6);
            ''', guild_id, None, None, None, None, '$')

    async def fetch_server_info(self, guild_id):
        async with self.bot.pool.acquire() as con:
            return await con.fetchrow('''
            SELECT * FROM termino_servers WHERE guild_id = $1;
            ''', guild_id)
            
    async def update_welcome_channel(self, guild_id, channel_id):
        async with self.bot.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET welcome_channel_id = $2 WHERE guild_id = $1;
            ''', guild_id, channel_id)

    async def update_welcome_role(self, guild_id, role_id):
        async with self.bot.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET welcome_role_id = $2 WHERE guild_id = $1;
            ''', guild_id, role_id)

    async def update_welcome_dm(self, guild_id, message):
        async with self.bot.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET welcome_dm = $2 WHERE guild_id = $1; 
            ''', guild_id, message)

    async def update_mute_role(self, guild_id, mute_role_id):
        async with self.bot.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET mute_role_id = $2 WHERE guild_id = $1;
            ''', guild_id, mute_role_id)

    async def update_prefix(self, guild_id, prefix):
        async with self.bot.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET prefix = $2 WHERE guild_id = $1;
            ''', guild_id, prefix)

    async def delete_row(self, guild_id):
        async with self.bot.pool.acquire() as con:
            await con.execute('''
            DELETE FROM termino_servers WHERE guild_id = $1;
            ''', guild_id)
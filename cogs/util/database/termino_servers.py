import asyncpg

class TerminoServers:

    def __init__(self, pool):
        self.pool = pool

    async def create_table(self):
        try:
            async with self.pool.acquire() as con:
                await con.execute('''
                CREATE TABLE termino_servers (
                    guild_id    BIGINT,
                    welcome_channel_id  BIGINT,
                    leave_channel_id BIGINT,
                    welcome_role_id BIGINT,
                    welcome_dm  TEXT,
                    mute_role_id    BIGINT
                );
                ''')
        except asyncpg.exceptions.DuplicateTableError:
            pass

    async def initialize_row(self, guild_id):
        async with self.pool.acquire() as con:
            await con.execute('''
            INSERT INTO termino_servers VALUES ($1, $2, $3, $4, $5, $6);
            ''', guild_id, None, None, None, None, None)

    async def fetch_server_info(self, guild_id):
        async with self.pool.acquire() as con:
            return await con.fetchrow('''
            SELECT * FROM termino_servers WHERE guild_id = $1;
            ''', guild_id)
            
    async def update_welcome_channel(self, guild_id, channel_id):
        async with self.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET welcome_channel_id = $2 WHERE guild_id = $1;
            ''', guild_id, channel_id)

    async def udpate_leave_channel(self, guild_id, channel_id):
        async with self.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET leave_channel_id = $2 WHERE guild_id = $1;
            ''', guild_id, channel_id)

    async def update_welcome_role(self, guild_id, role_id):
        async with self.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET welcome_role_id = $2 WHERE guild_id = $1;
            ''', guild_id, role_id)

    async def update_welcome_dm(self, guild_id, message):
        async with self.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET welcome_dm = $2 WHERE guild_id = $1; 
            ''', guild_id, message)

    async def update_mute_role(self, guild_id, mute_role_id):
        async with self.pool.acquire() as con:
            await con.execute('''
            UPDATE termino_servers SET mute_role_id = $2 WHERE guild_id = $1;
            ''', guild_id, mute_role_id)

    async def delete_row(self, guild_id):
        async with self.pool.acquire() as con:
            await con.execute('''
            DELETE FROM termino_servers WHERE guild_id = $1;
            ''', guild_id)
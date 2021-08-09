import asyncpg 

class DataBase:
    def __init__(self, user, passwd, host, port, database):
        self.dsn = f'postgres://{user}:{passwd}@{host}:{port}/{database}'  

    async def create_row(self, guild_id):
        async with asyncpg.create_pool(dsn = self.dsn) as pool:
            await pool.execute('''
            INSERT INTO termino_servers VALUES ($1, $2, $3, $4, $5);
            ''', guild_id, None, None, None, None)

    async def fetch_row(self, guild_id):
        async with asyncpg.create_pool(dsn = self.dsn) as pool:
            row = await pool.fetch('''
            SELECT * FROM termino_servers WHERE guild_id = $1;
            ''', guild_id)
            return row
            
    async def update_welcome_channel(self, guild_id, channel_id):
        async with asyncpg.create_pool(dsn = self.dsn) as pool:
            await pool.execute('''
            UPDATE termino_servers SET welcome_channel_id = $2 WHERE guild_id = $1;
            ''', guild_id, channel_id)

    async def update_welcome_role(self, guild_id, role_id):
        async with asyncpg.create_pool(dsn = self.dsn) as pool:
            await pool.execute('''
            UPDATE termino_servers SET welcome_role = $2 WHERE guild_id = $1;
            ''', guild_id, role_id)

    async def update_welcome_dm(self, guild_id, message):
        async with asyncpg.create_pool(dsn = self.dsn) as pool:
            await pool.execute('''
            UPDATE termino_servers SET welcome_dm = $2 WHERE guild_id = $1; 
            ''', guild_id, message)

    async def update_mute_role(self, guild_id, mute_role_id):
        async with asyncpg.create_pool(dsn = self.dsn) as pool:
            await pool.execute('''
            UPDATE termino_servers SET welcome_channel_id = $2 WHERE guild_id = $1;
            ''', guild_id, mute_role_id)

    async def delete_row(self, guild_id):
        async with asyncpg.create_pool(dsn = self.dsn) as pool:
            await pool.execute('''
            DELETE FROM termino_servers WHERE guild_id = $1;
            ''', guild_id)
class TerminoDbClient:
    def __init__(self, user, passwd, host, port, database):
        self.pool = None
        self.dsn = f'postgres://{user}:{passwd}@{host}:{port}/{database}'  

class TerminoServers(TerminoDbClient):

    async def initialize_server(self, guild_id):
        await self.pool.execute('''
        INSERT INTO termino_servers VALUES ($1, $2, $3, $4, $5);
        ''', guild_id, None, None, None, None)

    async def fetch_server_info(self, guild_id):
        row = await self.pool.fetch('''
        SELECT * FROM termino_servers WHERE guild_id = $1;
        ''', guild_id)
        return row
            
    async def update_welcome_channel(self, guild_id, channel_id):
        await self.pool.execute('''
        UPDATE termino_servers SET welcome_channel_id = $2 WHERE guild_id = $1;
        ''', guild_id, channel_id)

    async def update_welcome_role(self, guild_id, role_id):
        await self.pool.execute('''
        UPDATE termino_servers SET welcome_role_id = $2 WHERE guild_id = $1;
        ''', guild_id, role_id)

    async def update_welcome_dm(self, guild_id, message):
        await self.pool.execute('''
        UPDATE termino_servers SET welcome_dm = $2 WHERE guild_id = $1; 
        ''', guild_id, message)

    async def update_mute_role(self, guild_id, mute_role_id):
        await self.pool.execute('''
        UPDATE termino_servers SET mute_role_id = $2 WHERE guild_id = $1;
        ''', guild_id, mute_role_id)

    async def delete_row(self, guild_id):
        await self.pool.execute('''
        DELETE FROM termino_servers WHERE guild_id = $1;
        ''', guild_id)
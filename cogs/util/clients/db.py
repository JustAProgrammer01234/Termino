class DbClient:
    def __init__(self, pool):
        self.pool = pool 

    async def execute(self, query, *args):
        async with self.pool.acquire() as con:
            return await con.execute(query, args)

    async def fetch(self, query, *args):
        async with self.pool.acquire() as con:
            return await con.fetch(query, args)

    async def fetchrow(self, query, *args):
        async with self.pool.acquire() as con:
            return await con.fetchrow(query, args)

    async def fetch_server_info(self, guild_id):
        async with self.pool.acquire() as con:
            return await con.fetchrow('''
            SELECT * FROM termino_servers WHERE guild_id = $1;
            ''', guild_id)
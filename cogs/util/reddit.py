import asyncpraw

class TerminoReddit(asyncpraw.Reddit):
    def __init__(self, site_name):
        super().__init__(site_name = site_name)

    async def get_random_post(self, subreddit):
        pass 

    async def get_user_info(self, user):
        pass 

    async def get_subreddit_info(self, subreddit):
        pass 
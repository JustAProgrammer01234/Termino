import asyncpraw
from .corefuncs import random_choice

class TerminoReddit(asyncpraw.Reddit):
    def __init__(self, site_name):
        super().__init__(site_name = site_name)

    async def get_random_post(self, subreddit):
        memes = await self.subreddit(subreddit)
        meme = await random_choice([meme async for meme in memes.hot(limit=25)])
        submission = await self.submission(id = meme)
        return submission.title, submission.author, submission.url

    async def get_user_info(self, user):
        pass 

    async def get_subreddit_info(self, subreddit):
        pass 
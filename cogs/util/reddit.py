import os 
import apraw
import random 

class TerminoReddit(apraw.Reddit):
    def __init__(self):
        super().__init__(
            client_id = os.getenv("CLIENT_ID"),
            client_secret = os.getenv("CLIENT_SECRET"),
            user_agent = 'never gonna give you up',
            username = 'scripto_entity_1010',
            password = os.getenv('REDDIT_PASSWD')
        )

    async def get_meme(self):
        meme_subreddit = await self.subreddit("memes")
        meme = meme_subreddit.random()
        return meme.title, meme.url
import redditeasy
from .corefuncs import random_choice

class SubReddit(redditeasy.AsyncSubreddit):
    def __init__(self, client_id, client_secret, user_agent):
        super().__init__(client_id = client_id,
                client_secret = client_secret,
                user_agent = user_agent
            )

    async def get_random_post(self, subreddit):
        random_post = await self.get_post(subreddit = subreddit)
        while random_post.nsfw:
            random_post = await self.get_post(subreddit = subreddit)
        return random_post.title, random_post.author, random_post.content, random_post.post_url, random_post.score
        
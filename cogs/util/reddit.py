import redditeasy
from .corefuncs import random_choice

class SubReddit(redditeasy.AsyncSubreddit):
    def __init__(self, client_id, client_secret, user_agent):
        super().__init__(client_id = client_id,
                client_secret = client_secret,
                user_agent = user_agent
            )

    async def check_post(self, subreddit, post, new = False, top = False):
        while post.nsfw:
            if new:
                post = await self.get_new_post(subreddit = subreddit)
            elif top:
                post = await self.get_top_post(subreddit = subreddit)
            else:
                post = await self.get_post(subreddit = subreddit)
        return post.title, post.author, post.content, post.post_url, post.score

    async def get_random_post(self, subreddit):
        post = await self.get_post(subreddit = subreddit)
        return await self.check_post(subreddit, post, False, False)

    async def get_random_post_new(self, subreddit):
        post = await self.get_new_post(subreddit = subreddit)
        return await self.check_post(subreddit, post, True, False)

    async def get_random_post_top(self, subreddit):
        post = await self.get_top_post(subreddit = subreddit)
        return await self.check_post(subreddit, post, False, True)
import random
from discord.ext import commands

class SlapSomeone(commands.Converter):
    async def convert(self, ctx, reason):
        random_member = random.choice(ctx.guild.members)
        return f"{ctx.author} slapped {random_member} because of {reason}."

import random
from discord.ext import commands

class SlapSomeone(commands.Converter):
    async def convert(self, ctx, reason):
        member_list = ctx.guild.members
        slapped_member = random.choice(member_list)
        return f'{ctx.author.mention} slapped {slapped_member.mention} because of **{reason}**.'

def eightball(question):
    messages = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't count on it.",
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Replay hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.']

    return random.choice(messages), question

def is_even(num):
    num = int(num)
    return f'Yes `{num}` is even.' if num % 2 == 0 else f'Nope, `{num}` is not even.'
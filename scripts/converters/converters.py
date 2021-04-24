import random

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

    return random.choice(messages)

def is_even(num):
    num = int(num)
    return f'Yes `{num}` is even.' if num % 2 == 0 else f'Nope, `{num}` is not even.'

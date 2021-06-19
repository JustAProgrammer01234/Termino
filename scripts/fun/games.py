import random
import discord
from discord.ext import commands

class Games(commands.Cog):
    '''
    Commands related to games.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        player_dice = random.randint(1,6)
        bot_dice = random.randint(1,6)
        embed_color = random.randint(0x000000, 0xffffff)
        if player_dice == bot_dice:
            result_message = "Looks like it's a tie man."
        elif player_dice > bot_dice:
            result_message = 'Oh, looks like you won.'
        else:
            result_message = "Hahahah loser I won."
        result_embed = discord.Embed(title = result_message, color = embed_color)
        result_embed.add_field(name = 'You:', value = player_dice, inline = True)
        result_embed.add_field(name = 'Termino:', value = bot_dice, inline = True)
        await ctx.send(embed = result_embed)

    @commands.command(aliases = ['rps', 'rock-paper-scissors'])
    async def rock_paper_scissors(self, ctx, choice):
        choices = ['rock','paper','scissors']
        choices_emoji = {'rock':':rock:','paper':':newspaper:','scissors':':scissors:'}
        bot_choice = random.choice(choices)
        if choice in choices:
            if choice == bot_choice:
                await ctx.send("It's a tie.")
            elif choice == 'paper' and bot_choice == 'rock':
                await ctx.send('**You win!**, I chose :rock:')
            elif choice == 'scissors' and bot_choice == 'paper':
                await ctx.send('**You win!**, I chose :newspaper:')
            elif choice == 'rock' and bot_choice == 'scissors':
                await ctx.send('**You win!**, I chose :scissors:')
            else:
                await ctx.send(f'**Ah crap, you lost**, I chose {choices_emoji[bot_choice]}')
        else:
            await ctx.send('Your choice must be either rock, paper, or scissors.')

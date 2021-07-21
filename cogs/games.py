import random
import discord
from discord.ext import commands

class Games(commands.Cog):
    '''
    This category contains games.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        '''
        A command that allows you to play dice with you and Termino.
        '''
        player_dice = random.randint(1,6)
        bot_dice = random.randint(1,6)
        if player_dice == bot_dice:
            result_message = "Looks like it's a tie man."
        elif player_dice > bot_dice:
            result_message = 'Oh, looks like you won.'
        else:
            result_message = "LOL I won."
        result_embed = discord.Embed(title = result_message, color = 0xFFFF)
        result_embed.add_field(name = 'You:', value = player_dice, inline = True)
        result_embed.add_field(name = 'Termino:', value = bot_dice, inline = True)
        await ctx.send(embed = result_embed)

    @commands.command(aliases = ['rps', 'rock-paper-scissors'])
    async def rock_paper_scissors(self, ctx, choice):
        '''
        A command that allows you to play rock paper scissors with you and Termino.
        '''
        choices = ['rock','paper','scissors']
        choices_emoji = {'rock':':rock:','paper':':newspaper:','scissors':':scissors:'}
        bot_choice = random.choice(choices)
        if choice in choices:
            if choice == bot_choice:
                await ctx.send("It's a tie.")
            elif choice == 'paper' and bot_choice == 'rock':
                await ctx.send('**You win!**, I chose :rock:')
            elif choice == 'scissors' and bot_choice == 'paper':
                await ctx.send('**You win!** I chose :newspaper:')
            elif choice == 'rock' and bot_choice == 'scissors':
                await ctx.send('**You win!** I chose :scissors:')
            else:
                await ctx.send(f'**Ah crap, you lost**, I chose {choices_emoji[bot_choice]}')
        else:
            await ctx.send('`<choice>` must be either rock, paper, or scissors.')

def setup(bot):
    bot.add_cog(Games(bot))
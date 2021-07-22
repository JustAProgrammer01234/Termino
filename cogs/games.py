import random
import discord
import asyncio
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
            result_message = ":game_die: Looks like it's a tie man. :game_die:"
        elif player_dice > bot_dice:
            result_message = ':game_die: Oh, looks like you won. :game_die:'
        else:
            result_message = ":game_die: LOL I won. :game_die:"
        result_embed = discord.Embed(title = result_message, color = discord.Colour.random())
        result_embed.add_field(name = 'You:', value = player_dice, inline = True)
        result_embed.add_field(name = 'Termino:', value = bot_dice, inline = True)
        await ctx.send(embed = result_embed)

    @commands.command(name = 'rock-paper-scissors', aliases = ['rps'])
    async def rock_paper_scissors(self, ctx):
        '''
        A command that allows you to play rock paper scissors with you and Termino.
        '''
        bot_choice = random.choice(['rock','paper','scissors'])
        unicode_to_text = {
            '\U0001faa8':'rock',
            '\U0001f4f0':'paper',
            '\U00002702':'scissors'
        }

        def rps_check(reaction, user):
            valid_reactions = ['\U0001faa8','\U0001f4f0','\U00002702']
            return user == ctx.author and reaction.emoji in valid_reactions

        def check_winner(user_choice, bot_choice):
            user_wins = False 
            bot_wins = False 

            if user_choice == bot_choice:
                return user_wins, bot_wins, user_choice, bot_choice 
            elif user_choice == 'rock' and bot_choice == 'scissors':
                user_wins = True 
                return user_wins, bot_wins, user_choice, bot_choice 
            elif user_choice == 'paper' and bot_choice == 'rock':
                user_wins = True 
                return user_wins, bot_wins, user_choice, bot_choice 
            elif user_choice == 'scissors' and bot_choice == 'paper':
                user_wins = True 
            else:
                bot_wins = True 

            return user_wins, bot_wins, user_choice, bot_choice

        embd = discord.Embed(title = "I'll be waiting for only 1 minute.", color = discord.Colour.random())
        embd.add_field(name = 'React for:', value = ':rock: **->** `rock`\n:newspaper: **->** `paper`\n:scissors: **->** `scissors`')

        message = await ctx.send("I have chosen my move, you pick.")
        reaction_embed = await ctx.send(embed = embd)
        await reaction_embed.add_reaction('\U0001faa8')
        await reaction_embed.add_reaction('\U0001f4f0')
        await reaction_embed.add_reaction('\U00002702')

        try:
            choice, user = await self.bot.wait_for('reaction_add', timeout = 60.0, check = rps_check)
        except asyncio.TimeoutError:
            await message.delete()
            await reaction_embed.delete()
            await ctx.send('It took you too long to pick your choice. Try again.')
        else:
            await message.delete()
            await reaction_embed.delete()
            user_wins, bot_wins, user_choice, bot_choice = check_winner(unicode_to_text[choice.emoji], bot_choice)

            if user_wins == bot_wins:
                result_message = "It's a tie wtf."
            elif user_wins == True and bot_wins == False:
                result_message = "You win. Goddamnit."
            else:
                result_message = "You lose. I win lol."

            result_embed = discord.Embed(title = result_message, color = discord.Colour.random())
            result_embed.add_field(name = user, value = f'Choice picked:\n`{user_choice}` {choice.emoji}')

            if bot_choice == 'paper':
                result_embed.add_field(name = f'{self.bot.user.name}#{self.bot.user.discriminator}', value = f'Choice picked:\n`{bot_choice}` :newspaper:')
            else:
                result_embed.add_field(name = f'{self.bot.user.name}#{self.bot.user.discriminator}', value = f'Choice picked:\n`{bot_choice}` :{bot_choice}:')
            
            await ctx.send(embed = result_embed)
        
def setup(bot):
    bot.add_cog(Games(bot))
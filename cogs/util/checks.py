import discord 
from discord.ext import commands 

def has_mute_role():
    async def predicate(ctx):
        pass
    return commands.check(predicate) 

def is_muted():
    async def predicate(ctx):
        pass 
    return commands.check(predicate)

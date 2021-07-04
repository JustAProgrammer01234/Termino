from .fun import Fun
from .games import Games

def setup(bot):
    bot.add_cog(Fun(bot))
    bot.add_cog(Games(bot))
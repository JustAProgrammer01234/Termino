from .kickban import KickBan
from .mute import Mute

def setup(bot):
    bot.add_cog(KickBan(bot))
    bot.add_cog(Mute(bot))

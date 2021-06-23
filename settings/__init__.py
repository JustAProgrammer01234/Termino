from .joinsettings import JoinSettings
from .mutesettings import MuteSettings

def setup(bot):
    bot.add_cog(JoinSettings(bot))
    bot.add_cog(MuteSettings(bot))

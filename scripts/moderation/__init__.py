from . import mute
from . import joinsettings
from . import kickban

def add_command(bot):
    mute.add_command(bot)
    joinsettings.add_command(bot)
    kickban.add_command(bot)

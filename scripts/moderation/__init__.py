from .mute import *
from .kickban import *
from .joinsettings import *

def add_command(bot):
    bot.add_command(set_channel_join)
    bot.add_command(set_join_role)
    bot.add_command(delete_join_role)
    bot.add_command(delete_join_channel)
    bot.add_command(add_mute_role)
    bot.add_commsand(mute)
    bot.add_command(unmute)
    bot.add_command(kick)
    bot.add_command(ban)

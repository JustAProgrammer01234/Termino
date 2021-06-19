import discord
from .funcs import get_server_data

class UtilClass:
    def __init__(self, bot):
        self.bot = bot
        self.server_data = get_server_data('data.json')
        self.mp_manage_channels = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
            description = 'You are missing the `Manage Channels` permission.',
            color = discord.Colour.red()
        )
        self.mp_manage_messages = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
            description = 'You are missing the `Manage Messages` permission.',
            color = discord.Colour.red()
        )
        self.mp_manage_roles = discord.Embed(title = ':no_entry: Permission denied! :no_entry:',
            description = 'You are missing the `Manage Roles` permission.',
            color = discord.Colour.red()
        )
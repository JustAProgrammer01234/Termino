from .funcs import get_server_data

class UtilClass:
    def __init__(self, bot):
        self.bot = bot
        self.server_data = get_server_data('data.json')

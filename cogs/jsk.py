from jishaku.features.python import PythonFeature
from jishaku.features.root_command import RootCommand

class DebugCog(PythonFeature, RootCommand, name = 'debugging'):
    '''
    Command category for debugging
    '''
    def __str__(self):
        return ':computer: Debugging :computer:'

def setup(bot):
    bot.add_cog(DebugCog(bot=bot))
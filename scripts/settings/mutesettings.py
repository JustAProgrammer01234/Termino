from discord.ext import commands
from noncoroutines import change_server_data, UtilClass

class MuteSettings(UtilClass, commands.Cog):
    '''
    Commands related to settings for mute command.
    '''
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name = 'add-mute-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def add_mute_role(self, ctx, mute_role: commands.RoleConverter):
        self.server_data[str(ctx.guild.id)]['mute_role'] = mute_role.id
        change_server_data(self.server_data)
        ctx.send("Mute role has now been added.")

    @commands.command(name = 'remove-mute-role')
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def remove_mute_role(self, ctx):
        self.server_data[str(ctx.guild.id)]['mute_role'] = None
        change_server_data(self.server_data)
        ctx.send("Mute role has been removed.")
    
    @add_mute_role.error 
    async def add_mute_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_manage_roles)

    @remove_mute_role.error 
    async def add_mute_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.mp_manage_roles)
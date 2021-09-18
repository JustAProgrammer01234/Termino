import discord 
import inspect
import platform
from discord.ext import commands 

pong_url = 'https://media1.tenor.com/images/d43fa1f8705692a7907cf3952fd322e4/tenor.gif?itemid=14393751'

class Utility(commands.Cog):
    '''
    This category contains all useful commands.
    '''
    
    def __init__(self, bot):
        self.bot = bot

    def __str__(self):
        return ':white_check_mark: Utility :white_check_mark:'

    @commands.command()
    async def ping(self, ctx):
        '''
        Sends the latency of the bot
        '''
        embd = discord.Embed(title = 'Pong!', color = discord.Colour.from_rgb(255,255,255))
        embd.set_thumbnail(url = pong_url)
        embd.add_field(name = 'Latency:', value = f'`{self.bot.latency * 1000:.2f}ms`')

        await ctx.send(embed = embd)

    @commands.command()
    async def botinfo(self, ctx):
        '''
        Sends info about the bot.
        '''
        bot_dev = self.bot.get_user(self.bot.owner_id)
        bot_created_at = int(discord.utils.format_dt(self.bot.user.created_at))
        command_prefix = self.bot.command_prefix

        embd = discord.Embed(
            title = f'Info about: {self.bot.user}', 
            description = self.bot.description
        )
    
        embd.add_field(
            name = 'Developer:', 
            value = inspect.cleandoc(
                f'''**Username:** `{bot_dev}`
                **ID:** `{bot_dev.id}`
                '''
            ), 
            inline=False
        )

        embd.add_field(
            name = 'General info:', 
            value = inspect.cleandoc(
                f'''**Prefix:** `{command_prefix}`
                **Servers joined:** `{len(self.bot.guilds)}`
                **Bot created at:** {bot_created_at}
                '''
            ),
            inline=False 
        )

        embd.add_field(
            name = 'Library used:', 
            value = inspect.cleandoc(
                f'''**Name:** `discord.py`
                **Version:** `{discord.__version__}`
                '''
            ),
            inline=False
        )

        embd.add_field(
            name = 'Programming language used:', 
            value = inspect.cleandoc(
                f'''**Name:** `Python`
                **Version:** `{platform.python_version()}`
                '''
            ),
            inline=False
        )
        embd.set_thumbnail(url = self.bot.user.avatar.url)

        await ctx.send(embed = embd)

    @commands.command()
    async def source(self, ctx):
        '''
        Sends the source code of the bot.
        '''
        await ctx.send("https://github.com/JustAProgrammer01234/Termino")

    @commands.command() 
    @commands.guild_only()
    async def serverinfo(self, ctx):
        '''
        Sends info about the server. 
        '''
        len_text = len(ctx.guild.text_channels)
        len_voice = len(ctx.guild.voice_channels)
        len_users = len([user for user in ctx.guild.members if not user.bot])
        len_bots = len([user for user in ctx.guild.members if user.bot])
        len_emojis = len(ctx.guild.emojis)
        created_at = discord.utils.format_dt(ctx.guild.created_at.timestamp(), 'F')
        server_owner = self.bot.get_user(ctx.guild.owner_id)

        embd = discord.Embed(
            title = f'Info about server: {ctx.guild}', 
            description = f'''Server description: {ctx.guild.description}'''
        ) 

        embd.add_field(
            name = 'Owner:', 
            value = inspect.cleandoc(
                f'''**Username:** `{server_owner}`
                **Id:** `{server_owner.id}`
                '''
            ), 
            inline = False
        )

        embd.add_field(
            name = 'General info:', 
            value = inspect.cleandoc(
                f'''**Server created at:** {created_at}
                **Server ID**: `{ctx.guild.id}`
                **Region:** `{ctx.guild.region}`
                '''
            ), 
            inline = False
        )

        embd.add_field(
            name = 'Channel count:', 
            value = inspect.cleandoc(
                f'''**Text Channels:** `{len_text}`
                **Voice Channels:** `{len_voice}`
                **Total:** `{len_text + len_voice}`'''
            ),
            inline = False
        )

        embd.add_field(
            name = 'Member count:', 
            value = inspect.cleandoc(
                f'''**Users:** `{len_users}`
                **Bots:** `{len_bots}`
                **Total:** `{ctx.guild.member_count}`
                '''
            ), 
            inline = False
        )

        embd.add_field(
            name = 'Emoji count:', 
            value = inspect.cleandoc(
                f'''**Emoji limit:** `{ctx.guild.emoji_limit}`
                **Emojis:** `{len_emojis}`'''
            ), 
            inline = False
        )

        embd.set_thumbnail(url = ctx.guild.icon.url)

        await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    async def invitelink(self, ctx):
        '''
        Sends the bot's invite link.
        '''
        invite_url = discord.utils.oauth_url(client_id = '835062389078229032', permissions = discord.Permissions.all())
        await ctx.send(invite_url)

    @commands.command()
    @commands.guild_only() 
    async def memberinfo(self, ctx, member: commands.MemberConverter):
        '''
        Sends info about a member.
        '''
        member_roles = '\n'.join([role.mention for role in member.roles])
        member_created_at = discord.utils.format_dt(int(member.created_at.timestamp()), 'F')
        member_joined_at = discord.utils.format_dt(int(member.joined_at.timestamp()), 'F') 

        embd = discord.Embed(title = f'Info about member: {member}')

        embd.add_field(
            name = 'General info:', 
            value = inspect.cleandoc(
                f'''**Member created at:** {member_created_at}
                **User joined at:** {member_joined_at}
                **Member id:** `{member.id}`
                **Status:** `{member.status}`
                '''
            ), 
            inline = False
        )
        
        embd.add_field(
            name = 'Roles assigned:', 
            value = f'{member_roles}',
            inline = False
        )

        embd.set_thumbnail(url = member.avatar.url)

        await ctx.send(embed = embd)

    @commands.command(aliases = ['perm'])
    @commands.guild_only()
    async def permissions(self, ctx, member: commands.MemberConverter):
        perms = ''
        perms_embed = discord.Embed(title = f"{member}'s permissions.")

        for perm in member.guild_permissions:
            p = perm[0]
            if '_' in p:
                p = p.replace('_', ' ')
            p = p.title()
            perms += f'**`{p}`**\n'

        perms_embed.description = perms
        perms_embed.set_thumbnail(url = member.avatar.url)

        await ctx.send(embed = perms_embed)

    @commands.command(name = 'channel-permissions', aliases = ['channel-perm'])
    @commands.guild_only()
    async def channel_permissions(self, ctx, member: commands.MemberConverter):
        '''
        Sends every single perm a member has in the channel the command was called in.
        '''
        perms = ''
        perms_embed = discord.Embed(title = f"{member}'s permissions in {ctx.channel}.")

        for perm in member.permissions_in(ctx.channel):
            p = perm[0]
            if '_' in p:
                p = p.replace('_', ' ')
            p = p.title()
            perms += f'**`{p}`**\n'

        perms_embed.description = perms
        perms_embed.set_thumbnail(url = member.avatar.url)

        await ctx.send(embed = perms_embed)

def setup(bot):
    bot.add_cog(Utility(bot))
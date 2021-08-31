import discord 
import platform
from discord.ext import commands 

pong_url = 'https://media1.tenor.com/images/d43fa1f8705692a7907cf3952fd322e4/tenor.gif?itemid=14393751'

class Utility(commands.Cog, name = 'utility'):
    '''
    This command category contains all useful commands.
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
        command_prefix = self.bot.command_prefix

        embd = discord.Embed(
            title = f'Info about: {self.bot.user}', 
            description = self.bot.description, 
            color = discord.Colour.from_rgb(255,255,255)
        )
    
        embd.add_field(
            name = 'Developer:', 
            value = f'''
            **Username:** `{bot_dev}`
            **ID:** `{bot_dev.id}`''', 
            inline = False
        )

        embd.add_field(
            name = 'General info:', 
            value = f'''
            **Prefix:** `{command_prefix}`
            **Servers joined:** `{len(self.bot.guilds)}`
            **Bot created at:** `{self.bot.user.created_at.strftime('%d/%m/%Y')}`
            '''
        )

        embd.add_field(
            name = 'Library used:', 
            value = f'''
            **Name:** `discord.py`
            **Version:** `{discord.__version__}`''', 
            inline = False
        )

        embd.add_field(
            name = 'Programming language used:', 
            value = f'''
            **Name:** `Python`
            **Version:** `{platform.python_version()}`'''
        )

        embd.set_thumbnail(url = self.bot.user.avatar_url)

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
        server_owner = self.bot.get_user(ctx.guild.owner_id)

        embd = discord.Embed(
            title = f'Info about server: {ctx.guild}', 
            description = f'''Server description: {ctx.guild.description}''', 
            color = discord.Colour.from_rgb(255,255,255)
        ) 

        embd.add_field(
            name = 'Owner:', 
            value = f'''
            **Username:** `{server_owner}`
            **Id:** `{server_owner.id}`''', 
            inline = False
        )

        embd.add_field(
            name = 'General info:', 
            value = f'''**Server created at:** `{ctx.guild.created_at.strftime('%d/%m/%Y')}`
            **Server ID**: `{ctx.guild.id}`
            **Region:** `{ctx.guild.region}`''', 
            inline = False
        )

        embd.add_field(
            name = 'Channel count:', 
            value = f'''
            **Text Channels:** `{len_text}`
            **Voice Channels:** `{len_voice}`
            **Total:** `{len_text + len_voice}`''', 
            inline = False
        )

        embd.add_field(
            name = 'Member count:', 
            value = f'''**Users:** `{len_users}`
            **Bots:** `{len_bots}`
            **Total:** `{ctx.guild.member_count}`''', 
            inline = False
        )

        embd.add_field(
            name = 'Emoji count:', 
            value = f'''**Emoji limit:** `{ctx.guild.emoji_limit}`
            **Emojis:** `{len_emojis}`''', 
            inline = False
        )

        embd.set_thumbnail(url = ctx.guild.icon_url)

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
        perm_list = []

        for perm in member.permissions_in(ctx.channel):
            p = perm[0]
            if '_' in p:
                p = p.replace('_', ' ')
            p = p.title()
            perm_list.append(f'**`{p}`**')

        embd = discord.Embed(
            title = f'Info about member: {member}', 
            color = discord.Colour.from_rgb(255,255,255)
        )

        embd.add_field(
            name = 'General info:', 
            value = f'''**User created at:** `{member.created_at.strftime('%d/%m/%Y')}`
            **User joined at:** `{member.joined_at.strftime('%d/%m/%Y')}`
            **Member id:** `{member.id}`
            **Status:** `{member.status}`''', 
            inline = False
        )
        
        embd.add_field(
            name = 'Roles assigned:', 
            value = f'{member_roles}'
        )

        embd.add_field(
            name = 'Available perms:',
            value = '**,** '.join(perm_list)
        )

        embd.set_thumbnail(url = member.avatar_url)

        await ctx.send(embed = embd)

    @commands.command()
    @commands.guild_only()
    async def permissions(self, ctx):
        '''
        Sends every single perm the bot has.
        '''
        perms = ''
        perms_embed = discord.Embed(
            title = 'Permissions:',
            color = discord.Colour.from_rgb(255,255,255)
        )

        for perm in ctx.channel.permissions_for(ctx.me):
            p = perm[0]
            if '_' in p:
                p = p.replace('_', ' ')
            p = p.title()
            perms += f'**`{p}`**\n'

        perms_embed.description = perms
        perms_embed.set_thumbnail(url = self.bot.user.avatar_url)

        await ctx.send(embed = perms_embed)

def setup(bot):
    bot.add_cog(Utility(bot))
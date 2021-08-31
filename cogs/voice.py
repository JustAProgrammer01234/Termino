import re
import discord
from discord.ext import commands 

youtube_re = re.compile(r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$')

class Voice(commands.Cog, name = 'voice'):
    '''
    This category contains commands for voice channels.
    '''
    def __init__(self, bot):
        self.bot = bot 

    def __str__(self):
        return ':speaker: Voice :speaker:'

    @commands.command()
    @commands.guild_only()
    async def join(self, ctx):
        '''
        Joins the voice channel your in.
        '''
        voice = ctx.author.voice
        if voice:
            player = self.bot.wavelink.get_player(ctx.guild.id)
            await player.connect(voice.id)

            join_embed = discord.Embed(
                description = f"**Successfully connected to {voice.channel.mention}.**", 
                color = discord.Colour.green()
            )
        else:
            await ctx.send(":x: **Please join a voice channel.** :x:")
            
        await ctx.send(embed = join_embed)

    @commands.command()
    @commands.guild_only()
    async def spawn(self, ctx, voice_channel: commands.VoiceChannelConverter):
        '''
        Tells the bot to join a voice channel. 
        This is different to the join command because it does not go to the vc your in.
        '''
        player = self.bot.wavelink.get_player(ctx.guild.id)
        await player.connect(voice_channel.id)

        join_embed = discord.Embed(
            description = f"**Successfully connected to {voice_channel.mention}**",
            color = discord.Colour.green()
        )

        await ctx.send(embed = join_embed)

    @commands.command()
    @commands.guild_only()
    async def leave(self, ctx):
        '''
        Leaves the voice channel the bot is in.
        '''
        voice = ctx.voice_client 
        if voice:
            player = self.bot.wavelink.get_player(ctx.guild.id)
            await player.disconnect()
            leave_embed = discord.Embed(description = f"**Successfully left {voice.channel.mention}.**", color = discord.Colour.green())
        else:
            await ctx.send(":x: **Can't disconnect. I'm not currently in a voice channel.** :x:")

        await ctx.send(embed = leave_embed)

    @commands.command()
    @commands.guild_only()
    async def play(self, ctx, song):
        '''
        Plays the song in vc.
        The command will look through the yt search tab 
        if argument `song` is not a yt url like this:
        https://www.youtube.com/watch?v=dQw4w9WgXcQ
        '''
        player = self.bot.get_player(ctx.guild.id)

        if not player.is_connected:
            await ctx.invoke('join')

        if youtube_re.match(song) is None:
            yt_tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{song}')
        else:
            yt_tracks = await self.bot.wavelink.get_tracks(song)

        if not yt_tracks:
            return await ctx.send("Couldn't find the song you're looking for. Sorry.")
            
        print(yt_tracks)
        player.play(yt_tracks)
        

    @commands.command()
    @commands.guild_only()
    async def stop(self, ctx):
        '''
        Stops playing the song.
        '''
        player = self.bot.get_player(ctx.guild.id)
        await player.stop()

    @commands.command()
    @commands.guild_only()
    async def resume(self, ctx, url):
        '''
        Resumes playing the song.
        '''
        player = self.bot.get_player(ctx.guild.id)
        await player.set_pause(False)

    @commands.command()
    @commands.guild_only()
    async def pause(self, ctx):
        '''
        Pauses the song being played.
        '''
        player = self.bot.get_player(ctx.guild.id)
        await player.set_pause(True)

def setup(bot):
    bot.add_cog(Voice(bot))
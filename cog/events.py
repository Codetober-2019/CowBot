import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime
import os

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        servers = len(self.client.guilds)
        members = len(set(self.client.get_all_members()))
        activity = discord.Activity(name=f'{servers} servers with {members} members | a!help', type=discord.ActivityType.watching)
        channel = self.client.get_channel(612027042061615135)
        embed = discord.Embed(color=discord.Color.dark_green())
        embed.add_field(name="Joined a Server!", value=f"<:upvote:607776642189754368> AlphaIt just joined ***{guild.name}***. Now we are on ***{servers}*** servers.")
        await self.channel.send(embed=embed)
        await self.client.change_presence(activity=activity)
        
    @commands.Cog.listener()
    async def on_guild_leave(self, guild):
        servers = len(self.client.guilds)
        members = len(set(self.client.get_all_members()))
        activity = discord.Activity(name=f'{servers} servers with {members} members | a!help', type=discord.ActivityType.watching)
        channel = self.client.get_channel(612027042061615135)
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.add_field(name="Lefted a Server!", value=f"<:downvote:607777806922809366> AlphaIt just lefted ***{guild.name}***. Now we are on ***{servers}*** servers.")
        await channel.send(embed=embed)
        await self.client.change_presence(activity=activity)

    @commands.Cog.listener()
    async def on_error(self, ctx, error):
        print(error)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the requried argument.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("I don't have permission to do this.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("I can't do this.")
        

def setup(bot):
    bot.add_cog(events(bot))

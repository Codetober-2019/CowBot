import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime

class owner(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.is_owner()
    @commands.command()
    async def stop(self, ctx):
        await ctx.send("Stopped.")
        await self.client.logout()


        

def setup(bot):
    bot.add_cog(owner(bot))

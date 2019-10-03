import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime

class utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("MOOOOOOOOO it took `{}ms` for me to MOOOOOOO.".format(round(self.client.latency * 1000, 3)))

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name="CowBot Commands - pefix: `cow `")
        embed.add_field(name="Utility Commands:", value="`cow ping` - **Sends the bot latency.** `cow help` - **Shows this message**")
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(utilities(bot))

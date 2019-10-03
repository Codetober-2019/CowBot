import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime
import os


client = commands.Bot(command_prefix='cow ')
token = token
client.remove_command('help')

@client.event
async def on_ready():
    servers = len(client.guilds)
    members = len(set(client.get_all_members()))
    activity = discord.Activity(name=f'{servers} servers with {members} members | cow help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print(f"MOOOOOOO, I have booted as {client.user.name} ({client.user.id})")

@client.command()
async def ping(ctx):
    await ctx.send("MOOOOOOOOO it took `{}ms` for me to MOOOOOOO.".format(round(client.latency * 1000, 3)))
@client.command()
async def help(ctx):
    await ctx.send("MOOOOOOOO")
client.run(token)

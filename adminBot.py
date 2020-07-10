import discord
from discord.ext import commands
import requests
import os

payload = {}

client = commands.Bot(command_prefix = ';;')

@client.event
async def on_ready():
    activity = discord.Game(name=";;help", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Bot is ready')


@client.command()
async def help(ctx, *, link):
    
    await ctx.send(f';;help  -> help for use bot')

client.run('***********************') #BOT AUTH TOKEN
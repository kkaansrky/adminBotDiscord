import discord
from discord.ext import commands
import requests
import os
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member

payload = {}

client = commands.Bot(command_prefix = ';;')

@client.event
async def on_ready():
    activity = discord.Game(name=";;help", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Bot is ready')


@client.command()
async def hey(ctx):
    
    await ctx.send(f'hop')

@client.command()
async def mute(ctx, member: Member):
    guild = ctx.guild
    if(str(discord.utils.get(ctx.guild.roles, name="muted")) == "None"):
        await guild.create_role(name="muted")
        await ctx.channel.set_permissions(discord.utils.get(ctx.guild.roles, name="muted"), send_messages=False)

    
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    
    await(await ctx.send(f'muted')).delete(delay=3)

@client.command()
async def unmute(ctx, member: Member):
    guild = ctx.guild
  
    role = discord.utils.get(ctx.guild.roles, name="muted")
    
    await ctx.channel.set_permissions(role, send_messages=False)
    await member.remove_roles(role)
    
    await(await ctx.send(f'unmuted')).delete(delay=3)

client.run('**********') #BOT AUTH TOKEN
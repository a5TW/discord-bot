import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='_', intents=intents, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="poggers"))
    print(f'We have logged in as {client.user}')

@client.command()
async def ping(ctx):
    
    em = discord.Embed(title=f"Ping!",description=f'''Pong!''')
    await ctx.send(embed=em)

client.run(os.environ['DISCORD_TOKEN'])

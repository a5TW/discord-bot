import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='_', intents=intents, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(url="https://movies.lfdev.site", name="movies.lfdev.site"))
    print(f'We have logged in as {client.user}')

@client.command()
async def ping(ctx):
    
    await ctx.send("Pong!")

@client.command()
async def say(ctx, msg=None):
    if ctx.author.id == 773204048751886377 or ctx.author.id == 701621878631956572:
        await ctx.send(msg)
    else:
        await ctx.send('<:chuckle:1282380972087574609>')

client.run(os.environ['DISCORD_TOKEN'])

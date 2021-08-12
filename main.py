import discord, os, keep_alive, asyncio, datetime, pytz, requests

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=False
)

@client.event
async def on_ready(): 
    await client.change_presence(activity=discord.Game('Game-Name'), status=discord.Status.dnd)

keep_alive.keep_alive()
client.run(os.environ['TOKEN'], bot=False)
my_secret = os.environ['TOKEN']

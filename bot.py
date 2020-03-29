import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('BOT, RISE')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the Bridges!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hello, I've been waiting for you...")
    if message.content.startswith("what?"):
        await message.channel.send("That's right, I've been watching you...")
    if message.content.startswith("test"):
        await message.channel.send("Test running")

client.run('')

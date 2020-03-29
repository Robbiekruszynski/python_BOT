import discord
from discord.ext import commands
# import config
Bot = commands.Bot(command_prefix=" . ")
# client = discord.Client()
@Bot.event
async def on_ready():
    print(' bot is ready ')


@Bot.event
async def on_memeber_join(memeber):
    print(f'(memeber) has joined the One Million Developer Party!')


@Bot.event
async def on_message(message):
    message.content.lower()
    if message.author == Bot.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hello, I've been waiting for you...")
#     if message.content.startswith("what?"):
#         await message.channel.send("That's right, I've been watching you...")
#     if message.content.startswith("test"):
#         await message.channel.send("Test running")


Bot.run('')

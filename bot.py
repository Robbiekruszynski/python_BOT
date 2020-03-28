import discord
import config

client = discord.Client()
@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello?"):
        await message.channel.send("Hello, I've been waiting for you...")
    if message.content.startswith("what?"):
        await message.channel.send("That's right, I've been watching you...")
    if message.content.startswith("test"):
        await message.channel.send("Test running")


client.run(config.token)
# connection =S3Connection(config.token)


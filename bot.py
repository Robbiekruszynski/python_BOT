import discord
from discord.ext import commands


TOKEN = ""
client = discord.Client()


client = commands.Bot(command_prefix='!')


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


#     @client.event
#     async def on_member_join(self, member):
#         guild = member.guild
#         if guild.system_channel is not None:
#             to_send = 'Welcome {0.mention} to {1.name}! Have a look around and if you have any questions feel free to reach out to ADMINS'.format(
#                 member, guild)
#             await guild.system_channel.send(to_send)
# #

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("running?"):
        await message.channel.send("test bot running")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the One Million Developer discord!'
    )

# @client.command()
# async def foo(ctx):
#     await ctx.send('Hello')

client.run(TOKEN)

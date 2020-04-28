import discord
from discord.ext import commands
import random
TOKEN = ""

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_member_join(member):
    guild = member.guild
    arrival = ["Hi", "Hello", "Hey"]
    greeting = random.choice(arrival)

    if guild.system_channel is not None:
        to_send ='{2} {0.mention}, welcome to Teku! \nNew here? Introduce yourself in #introductions. \nTeku is an open source, eth2.0 client, written in Java created by the PegaSys team. \nUseful links: \nGithub: https://github.com/pegasyseng/ \ntekuDocs: https://docs.teku.pegasys.tech/en/latest/ ' \
                 '\nPegasys website: http://pegasys.tech/teku'.format(
            member, guild, greeting)
        welcome = list(filter(lambda x: x.name == 'welcome', guild.channels))[0]
        await welcome.send(to_send)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def lost(ctx):
    await ctx.send('This is a dedicated place to share efforts within the OMD community, take a look at the channels on the left column and check out any that look interesting to you! Always feel free to ping an Admin you see on the right column')

bot.run(TOKEN)

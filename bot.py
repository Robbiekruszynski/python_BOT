import discord
from discord.ext import commands
import random
TOKEN = "TOKEN"

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
    arrival = ["Hi", "Hello", "Welcome"]
    greeting = random.choice(arrival)

    if guild.system_channel is not None:
        to_send ='{2} {0.mention} to {1.name}! if you have any question please feel free to reach out to an Admin'.format(
            member, guild, greeting)
        welcome = list(filter(lambda x: x.name == 'welcome', guild.channels))[0]
        print(guild.channels)
        await welcome.send(to_send)
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def lost(ctx):
    await ctx.send('This is a dedicated place to share efforts within the OMD community, take a look at the channels on the left column and check out any that look interesting to you! Always feel free to ping an Admin you see on the right column')
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.command()
async def cool(ctx):
    await ctx.send('Not cool')





bot.run(TOKEN)

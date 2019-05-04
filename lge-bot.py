# Work with Python 3.6
import discord
from discord.ext import commands

TOKEN = ''


bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send("hello rs")


bot.run(TOKEN)

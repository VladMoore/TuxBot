import requests
import discord
from discord.ext import commands
import os
token = "" # Change
bot = commands.Bot(command_prefix = '[') # Change

@bot.event
async def on_ready():
    print("Bot Ready.")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(bot.latency * 1000)}ms')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)

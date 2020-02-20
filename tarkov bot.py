import asyncio
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="1")

@bot.event
async def on_ready():
    print("Connected and ready to use")

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(pass_context=True)
async def tarkov(ctx):
    await ctx.send(random.choice(["Shoreline",
                                  "Customs",
                                  "Reserve",
                                  "Interchange",
                                  "Woods :evergreen_tree:",
                                  "Smelliest person picks",]))

bot.run("Njc5MTcwNDczODQ1NTg3OTc4.Xk7jcA.bTsYuYf8dMAy0KTPohLXJ2mdAUM")

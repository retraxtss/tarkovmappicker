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

@bot.command(aliases=['tarkov'])
async def _8ball(ctx):
    await ctx.send(random.choice(["Shoreline :park:",
                                  "Customs :motorway:",
                                  "Reserve :coffin:",
                                  "Interchange :department_store:",
                                  "Woods :evergreen_tree:",
                                  "Smelliest person picks :sick:",]))

bot.run("Njc5MTcwNDczODQ1NTg3OTc4.Xk7oQw.WfTc6ToSInvjKcSK4pEKC6NHa8g")

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
async def rollcall(ctx):
    await ctx.send("Calling All Remy's @everyone")


@bot.command(pass_context=True)
async def tarkov(ctx):
    await ctx.send(random.choice(["Shoreline :park:",
                                  "Customs :motorway:",
                                  "Reserve :coffin:",
                                  "Interchange :department_store:",
                                  "Woods :evergreen_tree:",
                                  "Smelliest person picks :sick:", ]))


@bot.command(pass_context=True)
async def role(ctx):
    await ctx.send(random.choice(["Mid",
                                  "Top",
                                  "Jungle",
                                  "ADC",
                                  "Support",
                                  "Smelliest person picks :sick:", ]))
    

@bot.command(pass_context=True)
async def game(ctx):
    await ctx.send(random.choice(["Escape from Tarkov",
                                  "Call of Duty: Modern Warfare",
                                  "CS:GO",
                                  "League of Legends",
                                  "Halo Master Cheif Collection",
                                  "Rainbow Six Seige",
                                  "Duck Game",
                                  "Destiny 2",
                                  "Risk of Rain 2",
                                  "Smelliest person picks :sick:", ]))
    

@bot.command(pass_context=True)
async def nick(ctx)
    await ctx.send(random.choice(["Borderlands 3",
                                  "Jedi Fallen Order",
                                  "Dargonball Z",
                                  "Assassins Creed",
                                  "Doom Eternal",
                                  "MW2",]))




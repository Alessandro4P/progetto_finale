import discord
from discord.ext import commands
import os, random
from random import choice, randint
import time
from Speech import speech
from logic import minigioco
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def riciclo(ctx):
    await ctx.send(minigioco())


bot.run("MTIzODc5OTYwMzUwMzk4ODc3Ng.GoD-hn.E-XIJm9JO1JXMy-pNdeRzCA6AdCGabTdTahOOk")
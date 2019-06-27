import discord
from discord.ext import commands
import leagueColors
import os
import responder
import manager

#Constants
TEAM = "Team Horizon"

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

@client.command()
async def pro(ctx):
  color = leagueColors.PRO

@client.command()
async def semipro():
  color = leagueColors.SEMIPRO

@client.command()
async def amateur(ctx):
  color = leagueColors.AMATEUR
  await ctx.send(embed = responder.generateMatchEmbed(color, 3))

@client.command()
async def claim(context, message):
  color = leagueColors.AMATEUR
  author = context.message.author.name
  manager.set_player(int(message) - 1, author)
  await context.send(embed = responder.generateMatchEmbed(color, 3))

@client.command()
async def remove(context, message):
  color = leagueColors.AMATEUR
  author = context.message.author.name
  manager.remove_player(int(message) - 1, author)
  await context.send(embed = responder.generateMatchEmbed(color, 3))

TOKEN = os.getenv('BOT_TOKEN')
client.run(TOKEN)

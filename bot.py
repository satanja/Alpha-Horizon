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
async def semipro(ctx):
  color = leagueColors.SEMIPRO
  await ctx.send(embed = responder.generateMatchEmbed(color, 61, 2))

@client.command()
async def amateur(ctx):
  color = leagueColors.AMATEUR
  await ctx.send(embed = responder.generateMatchEmbed(color, 0, 3))

@client.command()
async def rookie(ctx):
  color = leagueColors.ROOKIE
  await ctx.send(embed = responder.generateMatchEmbed(color, 100, 4))

@client.command()
async def claimSemiPro(context, message):
  color = leagueColors.SEMIPRO


@client.command()
async def claimRookie(context, message):
  color = leagueColors.ROOKIE


@client.command()
async def remove(context, message):
  color = leagueColors.ROOKIE


TOKEN = os.getenv('BOT_TOKEN')
client.run(TOKEN)

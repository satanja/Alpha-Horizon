import discord
from discord.ext import commands
import leagueColors
import os
import responder

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
async def pro():
  color = leagueColors.PRO

@client.command()
async def semipro():
  color = leagueColors.SEMIPRO

@client.command()
async def amateur():
  color = leagueColors.AMATEUR
  await client.say(embed = responder.generateMatchEmbed(color, 3))

TOKEN = os.getenv('BOT_TOKEN')
client.run(TOKEN)
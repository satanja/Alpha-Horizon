import discord
from discord.ext import commands
import leagueColors
import os
import responder
from manager import Manager

#Constants
TEAM = "Team Horizon"

client = commands.Bot(command_prefix = '!')
semipro_manager = Manager(61)
rookie_manager = Manager(100)

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

@client.command()
async def pro(context):
  color = leagueColors.PRO

@client.command()
async def semipro(context, *args):
  color = leagueColors.SEMIPRO
  if len(args) != 0:
    author = context.message.author.name
    index = int(args[0]) - 1
    semipro_manager.set_player(index, author)
  await context.send(embed = responder.generateMatchEmbed(color, 61, 2, semipro_manager))

@client.command()
async def amateur(context, *args):
    print('not implemented')

@client.command()
async def rookie(context, *args):
  color = leagueColors.ROOKIE
  if len(args) != 0:
    author = context.message.author.name
    index = int(args[0]) - 1
    rookie_manager.set_player(index, author)
  await context.send(embed = responder.generateMatchEmbed(color, 100, 4, rookie_manager))

TOKEN = os.getenv('BOT_TOKEN')
client.run(TOKEN)

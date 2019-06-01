import scraper
import discord
import api
from match import Match
import manager

# returns the teams in a string
def formatTeams(match):
  return match.team1 + " vs " + match.team2

# returns the information in a string
def formatInfo(match):
  desc = "Channel: " + str(match.channel) + "\n"
  desc += "URL: " + str('https://alpha.tl/match/') + str(match.id)
  return desc


def formatMaps(match):

  result = ""
  players = manager.get_players()
  for i in range(0, 5):
    
    if players[i] == None:
      if (i == 4):
        result += "[ACE]: "
      else:
        result += "[" + str(i + 1) + "]: "
    else:
      result += players[i] + ": " 
    result += match.maps[i] + "\n"
  return result

def generateMatchEmbed(color, type):

  match = api.get_upcoming()

  embed = None
  if isinstance(match, str):
    color = 0xff0000
    embed = discord.Embed(title = match, color = color)
  else:
    title = formatTeams(match)
    desc = formatInfo(match)
    maps = formatMaps(match)
    embed = discord.Embed(title = title, description = desc, color = color)
    embed.add_field(name = "Maps", value = maps)
  return embed
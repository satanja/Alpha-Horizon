import scraper
import discord
import api
from match import Match
import manager

# returns the teams in a string
def formatTeams(match):
  return "{} vs {}".format(match.team1, match.team2)

# returns the information in a string
def formatInfo(match):
  url = 'https://alpha.tl/match/{}'.format(match.id)
  info = scraper.getBasicInfo(url)
  return "\n".join(info)


def formatMaps(match, manager):

  result = ""
  players = manager.get_players()
  for i in range(5):
    
    if players[i] == None:
      if (i == 4):
        result += "[ACE]: "
      else:
        result += "[{}]: ".format(i + 1)
    else:
      result += players[i] + ": " 
    result += match.maps[i] + "\n"
  return result

def generateMatchEmbed(color, teamId, type, manager):

  match = api.get_upcoming(teamId, type)
  if match == None:
    title = 'Error' + str(teamId)
    desc = 'No upcoming match found. Please wait until the next match becomes available.'
    embed = discord.Embed(title = title, description = desc, color = color)
    return embed
  else:
    title = formatTeams(match)
    desc = formatInfo(match)
    maps = formatMaps(match, manager)
    embed = discord.Embed(title = title, description = desc, color = color)
    embed.add_field(name = "Maps", value = maps)
    return embed
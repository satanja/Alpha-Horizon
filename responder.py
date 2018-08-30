import scraper
import discord

# returns the teams in a string
def formatTeams(teams):
  return teams[0] + " vs " + teams[1]

# returns the information in a string
def formatInfo(info):
  return "\n".join(info)

def formatMaps(maps):
  result = ""
  for i in range(0, 5):
    if (i == 4):
      result += "[ACE]: "
    else:
      result += "[" + str(i + 1) + "]: "
    result += maps[i] + "\n"
  return result

def generateMatchEmbed(color, type, team):

  details = scraper.getInfo(type, team)

  embed = None
  if isinstance(details, str):
    color = 0xff0000
    embed = discord.Embed(title = details, color = color)
  else:
    title = formatTeams(details[0])
    desc = formatInfo(details[1])
    maps = formatMaps(details[2])
    embed = discord.Embed(title = title, description = desc, color = color)
    embed.add_field(name = "Maps", value = maps)
  return embed
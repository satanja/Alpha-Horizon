import requests
import string
from bs4 import BeautifulSoup

# Constants
URL = "https://alpha.tl/"


# parsedPage = BeautifulSoup(page, 'html.parser')

def tournamentSelect(type):
  switcher = {
    1: "europro",
    2: "eurosemipro",
    3: "euroamateur",
    4: "eurookie"
  }
  return switcher.get(type, "invalid tournament type")

def teamSelect(teamId):
    switcher = {
        61: 'Team Ħorizon',
        100: 'Team Horizon Academy',
    }
    return switcher.get(teamId, "invalid teamId")

# parses the webpage using BeautifulSoup
def soupify(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  return soup

# finds the calendar of the webpage (output only <a> tags)
def getCalendar(url):
  soup = soupify(url)
  completeCalendar = list(soup.find(id="content"))[3]
  calendar = list(completeCalendar.find_all('a'))
  return calendar

# if no matches found: return 0
# if no matches remaining: return 1
# if there exists a match to be played: return url
def findNextTeamMatch(teamId, type):
  url = URL + tournamentSelect(type)
  calendar = getCalendar(url)
  team = teamSelect(teamId)
  
  matchList = []
  # find all instances of the matches the team has to play
  for entry in calendar:
    leftTeam = entry.find(class_="tablecol colw160 txtlgnright").get_text()
    rightTeam = entry.find(class_="tablecol colw160 txtlgnleft").get_text()
    if leftTeam == team or rightTeam == team:
      matchList.append(entry)
  
  if len(matchList) == 0:
    # no matches found that contain the team
    return 0
  else:
    for match in matchList:
      matchstatus = match.find(class_="tablecol colw55").get_text()
      if matchstatus == "-":
        # Found an uncompleted match
        # Return id
        return int(match['href'][-4:])
    # No uncompleted match remaining
    return 1

# Finds the both teams of the match and returns them in an array
def getTeams(url):
  matchPage = soupify(url)
  teams = []
  teamElements = list(matchPage.find_all(class_ = "matchclan"))
  for teamElement in teamElements:
    teams.append(teamElement.get_text())
  return teams

# Finds the date, time, and chat channel on the webpage.
# The are returned in an array together with the url of the webpage
def getBasicInfo(url):
  matchPage = soupify(url)
  info = []
  infoElements = list(matchPage.find_all(class_="matchinfo-info"))
  for i in range(3):
    info.append(infoElements[i].get_text())
  info.append(url)
  return info

# Finds the maps of the match and returns them in an array
def getMaps(url):
  matchPage = soupify(url)
  maps = []
  mapElements = list(matchPage.find_all(class_="match-pregame-map"))
  for mapElement in mapElements:
    mapString = string.capwords(mapElement.get_text().lower())
    maps.append(mapString)
  return maps
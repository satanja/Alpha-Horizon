import requests
import json
import scraper
from match import Match

UPCOMING = 'https://alpha.tl/api?upcomingmatches'
MATCH_PREFIX = 'https://alpha.tl/api?match=' 
TEAM_ID = 61

def get_upcoming():
    
    response = requests.get(UPCOMING)
    upcoming_matches = json.loads(response.text)

    id = None

    for match in upcoming_matches:
        if match["team1"]["id"] == TEAM_ID or match["team2"]["id"] == TEAM_ID:
            id = match["id"]
    
    if id == None:
        id = scraper.findNextTeamMatch()
    
    if id == 0 or id == 1: 
        return None

    match_url = MATCH_PREFIX + str(id)
    response = requests.get(match_url)
    upcoming_match = json.loads(response.text)

    channel = upcoming_match["channel"]
    datetime = upcoming_match["datetime"]
    team1 = upcoming_match["team1"]["name"]
    team2 = upcoming_match["team2"]["name"]
    maps = upcoming_match["maps"]

    result = Match(id, channel, datetime, team1, team2, maps)

    # print(upcoming_match)
    return result
    
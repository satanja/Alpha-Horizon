import requests
import json
import scraper
import manager
from typing import Union
from match import Match

UPCOMING = "https://alpha.tl/api?upcomingmatches"
MATCH_PREFIX = "https://alpha.tl/api"

def get_upcoming(teamId, type, manager) -> Union[Match, None]:
    
    response = requests.get(UPCOMING)
    upcoming_matches = json.loads(response.text)

    match_id = None

    for match in upcoming_matches:
        if match["team1"]["id"] == teamId or match["team2"]["id"] == teamId:
            match_id = match["id"]
    
    if match_id == None:
        match_id = scraper.findNextTeamMatch(teamId, type)
    
    if match_id in [0, 1]: 
        return None

    match_url = MATCH_PREFIX
    params = {"match": str(match_id)}
    response = requests.get(match_url, params=params)
    upcoming_match = json.loads(response.text)

    channel = upcoming_match["channel"]
    datetime = upcoming_match["datetime"]
    team1 = upcoming_match["team1"]["name"]
    team2 = upcoming_match["team2"]["name"]
    maps = upcoming_match["maps"]

    result = Match(match_id, channel, datetime, team1, team2, maps)
    
    if manager.is_new_match(result):
        print("clearing...")
        manager.clear_saved_match(result.id)
        
    # print(upcoming_match)
    return result
    
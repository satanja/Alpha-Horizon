import api
import json
from match import Match

with open('match.json') as file:
    data = file.read()

saved_match = json.loads(data)

def save_data(): 
    with open('match.json', 'w') as outfile:
        json.dump(saved_match, outfile)

def set_player(map_id, player):
    global saved_match

    new_match = api.get_upcoming()
    if saved_match['id'] != new_match.id and new_match != None:
        saved_match['id'] = new_match.id
        saved_match['claims'] = [None] * 5

    saved_match['claims'][map_id] = player
    save_data()

def remove_player(map_id, player):
    if saved_match['claims'][map_id] == player:
        saved_match['claims'][map_id] = None
        save_data()

def get_players():
    return saved_match['claims']
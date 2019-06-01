import api
from match import Match

saved_match = api.get_upcoming()
players = [None] * 5

def set_player(map_id, player):
    global saved_match
    global players

    new_match = api.get_upcoming()
    if saved_match.id != new_match.id:
        saved_match = new_match
        players = [None] * 5

    players[map_id] = player

def remove_player(map_id, player):
    if players[map_id] == player:
        players[map_id] = None

def get_players():
    return players
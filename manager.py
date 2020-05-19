import api
import json
from match import Match

class Manager:
    def __init__(self, teamId):
        self.teamId = teamId
        self.players = [None] * 5
        self.lastMatchId = 0

    def is_new_match(self):
        print("not implemented")

    def set_player(self, map_id, player):
        self.players[map_id] = player

    def get_players(self):
        return self.players
    
    def clear_saved_match(self):
        self.players = [None] * 5

    def print(self):
        print(self.teamId)
saved_match = None

# def load_saved_match():
#     with open('match.json') as match_file:
#         data = match_file.read()
#     global saved_match
#     saved_match = json.loads(data)

# load_saved_match()

# def save_data(): 
#     with open('match.json', 'w') as outfile:
#         json.dump(saved_match, outfile, indent=4)

# def set_player(map_id, player):
#     global saved_match 
#     saved_match = load_saved_match()

#     new_match = api.get_upcoming()
#     if is_new_match(new_match):
#         clear_saved_match(new_match.id)

#     saved_match['claims'][map_id] = player
#     save_data()

# def remove_player(map_id, player):
#     if saved_match['claims'][map_id] == player:
#         saved_match['claims'][map_id] = None
#         save_data()

# def get_players():
#     return saved_match['claims']

# def is_new_match(match):
#     return match is not None and saved_match['id'] != match.id

# def clear_saved_match(new_id):
#     saved_match['id'] = new_id
#     saved_match['claims'] = [None] * 5
#     save_data()

from ast import List
from models.tournament import Tournament
from models.match import Match
from views.roundview import RoundView   
import json
  
class RoundController():
    
    def __init__(self):
            pass
    def create_round (self,tournament):
        print("ligne 12 round_controller",tournament)
        count = int(tournament.get("numero_round_actif"))
        player_list_file = tournament.get("liste_des_joueurs")
        with open(player_list_file, "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)
        list_players: List= player_data
        self.name = "Round" + str(count)
        self.nbmatch = len(list_players)/2
        if count == 1:
            for player in tournament.tournament_players_list():
                match = Match()
                match.player1 = player
                for playertwo in range(list_players.index(player),len(list_players)):
                    match.player2 = playertwo

                round_list = []    
                new_round_match_file = {
                    "id_round": tournament.get(id_tournoi) + "_" + str(count),
                    "match" : match                                
                }
                round_list.append(new_round_match_file)

            file_path = 'data/rounds/' + tournament.tournament_id + self.name + '.json'
            with open(file_path, 'x') as file:
                json.dump(round_list, file)     
            RoundView.display_round1_create(self)
from ast import List
import random
import json
from typing import Any, Dict
from models.tournament import Tournament
from models.match import Match
from views.roundview import RoundView   
import json
class MatchEncoder(json.JSONEncoder):
        "sert à la serialisation des matchs dans le fichier json"
        def default(self, o: Any) -> Dict[str, Any]:
            if isinstance(o, Match):
                return {
                    "player1": o.players[0],
                    "player2": o.players[1],
                    "score1": o.scores[0],
                    "score2": o.scores[1]
                }
            return super().default(o)  
class RoundController():
    
    def __init__(self):
            pass
        
    def create_round(self, tournament):
        count = int(tournament.get("numero_round_actif"))
        player_list_file = tournament.get("liste_des_joueurs")

        with open(player_list_file, "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)

        list_players = player_data

        self.name = "Round" + str(count)
        self.nbmatch = len(list_players) / 2
        round_list = []
        # Si on crée le poremier round
        if count == 1:
            random.shuffle(list_players)
            match_list = []
            for index_list_player, index_list_playertwo in zip(range(0, len(list_players), 2), range(1, len(list_players), 2)):
                match_player1 = list_players[index_list_player]
                match_player2 = list_players[index_list_playertwo]

                match = Match(match_player1, match_player2)

                new_round_match_file = {
                    "id_round": tournament.get("id du tournoi") + "_" + str(count),
                    "match": match
                }
                match_list.append(new_round_match_file)

            round_list.append(match_list)
            file_path = 'data/rounds/' + tournament.get("id du tournoi") + self.name + '.json'
            with open(file_path, 'x') as file:
                json.dump(match_list, file, cls=MatchEncoder, indent=2)
        """else:
            # Tri des joueurs par score puis par ordre d'ajout (dans le cas où plusieurs joueurs ont le même score)
            sorted_players = sorted(list_players, key=lambda, match_list.get("score")))
            list_players = sorted_players.copy()"""
        
        RoundView.display_round1_create(self)
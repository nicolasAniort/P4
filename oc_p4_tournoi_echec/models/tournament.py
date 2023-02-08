import json
from models.player import Player
from models.round import Round
from typing import List
import datetime

class Tournament:
    """
    Definition d'un tournoi: 
    nom, lieu, date de debut, date de fin, nombre de tour,  
    """
    def __init__(self, name: str, location: str, start_date: datetime.date, end_date: datetime.date, nb_round: int ,num_round: int , players: List[Player], stage: List[Round], ranking: List[int], notes: str = ""):
        nb_round = 0
        num_round = 0
        self.players = []
        if (len(players) % 2) == 0 and len(players)> 4 :
            nb_round = len(players) /2
        elif (len(players) % 2) != 0 and len(players)> 4 : 
            nb_round = len(players) + 0.5
        else :
            nb_round = 4
        self.nb_round = nb_round
        self.num_round = 1
        self.stage = stage
        self.rank = ranking
        self.notes = notes
        
    def add_round(self, round: Round):
        self.stage.append(round)
        
    def add_player(self, player: Player):
        self.players.append(player)
        
    def get_player_by_id(self, player_id: str) -> Player:
        for player in self.players:
            if player.id == player_id:
                return player
        return None
    
    def get_players_sorted_by_score(self) -> List[Player]:
        return sorted(self.players, key=lambda x: x.score, reverse=True)

    def to_json(self) -> str:
        data = self.__dict__.copy()
        data["stage"] = [stage.to_json() for stage in data["stage"]]
        data["players"] = [player.to_json() for player in data["players"]]
        return json.dumps(data)
    
    @staticmethod
    def from_json(json_str: str) -> "Tournament":
        data = json.loads(json_str)
        data["stage"] = [Round.from_json(r) for r in data["stage"]]
        data["players"] = [Player.from_json(p) for p in data["players"]]
        return Tournament(**data)
import json
from models.player import Player
from models.round import Round
from typing import List
import datetime

class TournamentEmpty:
    """
    Definition d'un tournoi: 
    nom, lieu, date de debut, date de fin, nombre de tour,  
    """
    def __init__(self, name: str, location: str, start_date: datetime.date, end_date: datetime.date, notes: str = ""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.notes = notes
        print("Le tournoi ",name,"est pret à être peuplé")

          
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
    def from_json(json_str: str) -> "TournamentEmpty":
        data = json.loads(json_str)
        data["stage"] = [Round.from_json(r) for r in data["stage"]]
        data["players"] = [Player.from_json(p) for p in data["players"]]
        return Tournament(**data)
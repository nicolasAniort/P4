import json
from models.player import Player
from models.round import Round
from typing import List

class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, rounds: List[Round], players: List[Player], notes: str = ""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.players = players
        self.notes = notes
        
    def add_round(self, round: Round):
        self.rounds.append(round)
        
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
        data["rounds"] = [round.to_json() for round in data["rounds"]]
        data["players"] = [player.to_json() for player in data["players"]]
        return json.dumps(data)
    
    @staticmethod
    def from_json(json_str: str) -> "Tournament":
        data = json.loads(json_str)
        data["rounds"] = [Round.from_json(r) for r in data["rounds"]]
        data["players"] = [Player.from_json(p) for p in data["players"]]
        return Tournament(**data)
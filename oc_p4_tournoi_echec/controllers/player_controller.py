from typing import List
from models.player import Player
from views.player_view import PlayerView

class PlayerController:
    
    def __init__(self, players: List[Player]):
        self.players = players
        self.player_view = PlayerView(self.players)

    def list(self) -> str:
        return self.player_view.list()

    def get(self, id: int) -> str:
        return self.player_view.get(id)

    def add(self, player: Player) -> None:
        self.players.append(player)
        self.players = sorted(self.players, key=lambda p: p.name)

    def remove(self, id: int) -> None:
        self.players = [p for p in self.players if p.id != id]
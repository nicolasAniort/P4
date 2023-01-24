from typing import List
from models.round import Round
from views.round_view import RoundView

class RoundController:
    def __init__(self, rounds: List[Round]):
        self.rounds = rounds
        self.round_view = RoundView(self.rounds)

    def list(self) -> str:
        return self.round_view.list()

    def get(self, id: int) -> str:
        return self.round_view.get(id)

    def add(self, round: Round) -> None:
        self.rounds.append(round)

    def remove(self, id: int) -> None:
        self.rounds = [r for r in self.rounds if r.id != id]
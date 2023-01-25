import json

class Round:
    from datetime import datetime

class Tour:
    def __init__(self, name: str):
        self.name = name
        self.matches = []
        self.start_time = None
        self.end_time = None

    def add_match(self, player1: Player, score1: int, player2: Player, score2: int):
        self.matches.append(([player1, score1], [player2, score2]))

    def start(self):
        self.start_time = datetime.now()

    def end(self):
        self.end_time = datetime.now()
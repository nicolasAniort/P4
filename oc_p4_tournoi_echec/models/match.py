import json
from models.player import Player
#from models.round import Round

class Match:
    def __init__(self, player1: Player, player2: Player, score1: int, score2: int, tuplet):
        
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.list_player_round = [player1,player2]
        self.list_score_round = [score1,score2]
        self.tuplet = (self.list_player_round,self.list_score_round)

    """test du gagnant: celui dont le score est supérieur à l'autre est le vainqueur!"""
    def winner(self) -> Player:
        if self.score1 > self.score2:
            return self.player1
        elif self.score2 > self.score1:
            return self.player2
        return None

    """test du perdant: celui dont le score est inférieur à l'autre est le vaincu!"""
    
    def loser(self) -> Player:
        if self.score1 < self.score2:
            return self.player1
        elif self.score2 < self.score1:
            return self.player2
        return None

    """test du match nul: si les score sont les memes , alors le test sera vrai!"""

    def neutral(self) -> bool:
        return self.score1 == self.score2

    """La méthode statique sert à """

    @staticmethod
    def from_json(json_str: str) -> 'Match':
        data = json.loads(json_str)
        return Match(Player.from_json(data['player1']), Player.from_json(data['player2']), data['score1'], data['score2'])
    
    def to_json(self) -> str:
        return json.dumps({'player1': self.player1.to_json(), 'player2': self.player2.to_json(), 'score1': self.score1, 'score2': self.score2})
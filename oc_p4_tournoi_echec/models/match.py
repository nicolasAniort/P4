class Match:
    def __init__(self, player1: Player, player2: Player, score1: int, score2: int):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
    
    def winner(self) -> Player:
        if self.score1 > self.score2:
            return self.player1
        elif self.score2 > self.score1:
            return self.player2
        return None
    
    def loser(self) -> Player:
        if self.score1 < self.score2:
            return self.player1
        elif self.score2 < self.score1:
            return self.player2
        return None
    
    def draw(self) -> bool:
        return self.score1 == self.score2
    
    @staticmethod
    def from_json(json_str: str) -> 'Match':
        data = json.loads(json_str)
        return Match(Player.from_json(data['player1']), Player.from_json(data['player2']), data['score1'], data['score2'])
    
    def to_json(self) -> str:
        return json.dumps({'player1': self.player1.to_json(), 'player2': self.player2.to_json(), 'score1': self.score1, 'score2': self.score2})
class Match:
    def __init__(self, player1, player2, score1=None, score2=None):
        self.players = [player1, player2]
        self.scores = [score1, score2]

    def __repr__(self):
        return f"<Match: {self.players[0]} contre {self.players[1]}>"
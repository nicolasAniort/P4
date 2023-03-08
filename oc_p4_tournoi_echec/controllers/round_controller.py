from models.tournament import Tournament
from models.match import Match
  
    def __init__(self):
        pass
    def create_round (self,tournament:Tournament):
        count = tournament.tournament_number_of_round()
        list_players = tournament.tournament_players_list()
        self.name = "Round" + str(count)
        self.nbmatch = len(tournament.tournament_players_list())/2
        if count == 1:
            for player in tournament.tournament_players_list():
                match = Match()
                match.player1 = player
                for playertwo in range(list_players.index(player),len(tournament.tournament_players_list())):
                    match.player2 = playertwo
                    
    
    
    
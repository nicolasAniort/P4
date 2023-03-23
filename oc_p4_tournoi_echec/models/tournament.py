from datetime import datetime


class Tournament:

    """initialisation du constructeur de tournoi"""

    def __init__(
        self,
        tournament_id: None,
        tournament_name: str,
        tournament_location: str,
        tournament_date_start: datetime,
        tournament_date_end: datetime,
        tournament_number_of_round: int,
        tournament_description: str,
        tournament_round_number: int,
        tournament_round_list=[],
        tournament_players_list=[],
    ):
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.tournament_date_start = tournament_date_start
        self.tournament_date_end = tournament_date_end
        self.tournament_number_of_round = tournament_number_of_round
        self.tournament_description = tournament_description
        self.tournament_round_number = tournament_round_number
        self.tournament_round_list = tournament_round_list
        self.tournament_players_list = tournament_players_list

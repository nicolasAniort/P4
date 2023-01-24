from typing import List
from models.tournament import Tournament
from models.player import Player
from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController
from views.player_view import PlayerView

class TournamentController:
    def __init__(self, tournaments: List[Tournament], players: List[Player]):
        self.tournaments = tournaments
        #self.player = PlayerView()
        #self.player = PlayerView(players)
        self.player = players
        self.player_view = PlayerView(self.players)
        self.options = {
            'a': self.add_player(),
            'p': self.display_players(),
            'l': self.list_players(),
            't': self.create_tournament(),
            'T': self.display_tournaments(),
            's': self.select_tournament(),
            'g': self.generate_pairs(),
            'r': self.display_results()
        }
    def add_player(self):
        player_controller = PlayerController(self.player.show_create_player())
        player_controller.add(player_controller.get_input())
        
    def display_players(self):
        player_controller = PlayerController(self.tournament.players)
        player_controller.list()

    def list_players(self):
        player_controller = PlayerController(self.tournament.players)
        player_controller.list()

    def list(self) -> str:
        return self.tournament_view.list()

    def get(self, id: int) -> str:
        return self.tournament_view.get(id)

    def add(self, tournament: Tournament) -> None:
        self.tournaments.append(tournament)
        self.tournaments = sorted(self.tournaments, key=lambda t: t.name)

    def remove(self, id: int) -> None:
        self.tournaments = [t for t in self.tournaments if t.id != id]

    def create_tournament(self):
        name = input("Entrez le nom du tournoi: ")
        location = input("Entrez l'emplacement du tournoi: ")
        start_date = input("Entrez la date de début du tournoi (jj/mm/aaaa): ")
        end_date = input("Entrez la date de fin du tournoi (jj/mm/aaaa): ")
        # On crée un objet Tournament avec les informations saisies
        self.tournament = Tournament(name, location, start_date, end_date)
        self.players = []
        self.rounds = []
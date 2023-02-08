import json
import os
from typing import List
from models.tournament import Tournament
from models.player import Player
from controllers.player_controller import PlayerController
from views.player_view import PlayerView
from views.tournament_view import TournamentView

filepath_tournament = "C:/Users/conta/OneDrive/PROJETS_DEV/1-OC_PYTHON/PROJ4/DEV/PROJ4/oc_p4_tournoi_echec/data/tournaments/files.json"

def load_tournament(filepath_tournament):
        """
        Charge un tournoi à partir d'un fichier JSON
        :param filepath: Chemin vers le fichier JSON à charger
        :return: Un objet Tournament ou None si le fichier est vide ou ne contient pas de données valides
        """
        print(filepath_tournament)
        if not os.path.isfile(filepath_tournament):
            open(filepath_tournament, 'w').close()
        try:
            with open(filepath_tournament, 'r') as f:
                #json_data = json.load(f)
                json_data = f.read()
            tournament = Tournament.from_json(json_data)
        except json.decoder.JSONDecodeError:
            tournament = None
        return tournament

class TournamentController:
    def __init__(self, players: List[Player]):
        self.tournaments = load_tournament(filepath_tournament)
        self.tournament_view = TournamentView(self.tournaments)
        self.player = players
        self.player_view = PlayerView(players)
        self.options = {
            '1': self.create_tournament(),
            '2': self.add_player(),
            '3': self.create_round(),
            '4': self.list_players(),
            'T': self.tournament_view.display_tournaments(),
            's': self.select_tournament,
            'g': self.generate_pairs(),
            'r': self.display_results()
        }
    def add_player(self):
        player_controller = PlayerController(self.player)
        player_controller.add_player(player_controller.get_input())
        
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
        self.players = []
        self.nb_rounds = 4
        self.num_round = Tournament.num_round
        #self.tournament = Tournament(name, location, start_date, end_date)
    
    def load_tournament(filepath_tournament):
        """
        Charge un tournoi à partir d'un fichier JSON
        :param filepath: Chemin vers le fichier JSON à charger
        :return: Un objet Tournament ou None si le fichier est vide ou ne contient pas de données valides
        """
        print(filepath_tournament)
        if not os.path.isfile(filepath_tournament):
            open(filepath_tournament, 'w').close()
        try:
            with open(filepath_tournament, 'r') as f:
                #json_data = json.load(f)
                json_data = f.read()
            tournament = Tournament.from_json(json_data)
        except json.decoder.JSONDecodeError:
            tournament = None
        return tournament
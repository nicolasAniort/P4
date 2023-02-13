import json
import os
from typing import List
from models.tournament import Tournament
from models.player import Player
from controllers.player_controller import PlayerController
from views.player_view import PlayerView
from views.tournament_view import TournamentView


filepath_tournament = "C:/Users/conta/OneDrive/PROJETS_DEV/1-OC_PYTHON/PROJ4/DEV/PROJ4/oc_p4_tournoi_echec/data/tournaments/files.json"

class TournamentEmptyController:
   
    def __init__(self):
        
        self.tournament_view = TournamentView(self.tournament_view)
        self.options = {
                '1': self.create_tournamentempty,
                '2': self.tournament_view.display_submenufilling,
                '3': self.tournament_view.display_managedtournament,
                
            }
    def display_submenufilling(self):
        self.tournament_view.display_submenufilling()

    def display_managedtournament(self):
        self.tournament_view.display_managedtournament(self)
    
    def create_tournamentempty(self):
            name = input("Entrez le nom du tournoi: ")
            location = input("Entrez l'emplacement du tournoi: ")
            start_date = input("Entrez la date de début du tournoi (jj/mm/aaaa): ")
            end_date = input("Entrez la date de fin du tournoi (jj/mm/aaaa): ")
            notes = input("Entrez les annotations spécifiques au tournoi:")


class TournamentController(TournamentEmptyController):
   
    def __init__(self, tournament: Tournament, filepath: str):
        self.filepath = filepath
        self.tournament = tournament
        self.tournament_view = TournamentView(self)
        self.player_controller = PlayerController(self)
        self.player_view = PlayerView(self)
        self.options = {
            '1': self.create_tournamentempty,
            '2': self.display_submenufilling,
            '3': self.display_managedtournament,
            '4': self.add_player,
            '5': self.update_player,
            '6': self.remove_player,
            '7': self.display_players,
            '8': self.exit,
        }

    def add_player(self):
        self.player_controller.add_player()

    def update_player(self):
        self.player_controller.update_player()

    def remove_player(self):
        self.player_controller.remove_player()

    def display_players(self):
        self.player_view.display_players(self.tournament.players)

    def exit(self):
        self.tournament.to_json(self.filepath)
        print("Tournoi sauvegardé.")
        raise SystemExit
                
    """def load_tournament(filepath_tournament):
            
            Charge un tournoi à partir d'un fichier JSON
            :param filepath: Chemin vers le fichier JSON à charger
            :return: Un objet Tournament ou None si le fichier est vide ou ne contient pas de données valides
            
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
            return tournament"""
    def load_tournament(filepath_tournament):
            """
            Charge un tournoi à partir d'un fichier JSON
            :param filepath: Chemin vers le fichier JSON à charger
            :return: Un objet Tournament ou None si le fichier est vide ou ne contient pas de données valides
            """
            
            if not os.path.isfile(filepath_tournament):
                open(filepath_tournament, 'w').close()

            try:
                with open(filepath_tournament, 'r') as f:
                    json_data = f.read()
                tournament = Tournament.from_json(json_data)
            except json.decoder.JSONDecodeError:
                tournament = None
            
            return tournament

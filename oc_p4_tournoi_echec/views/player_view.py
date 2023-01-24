from typing import List
from models.player import Player

class PlayerView:
    def __init__(self, players: List[Player]):
        self.players = players
        """
        initialisation du constructeur
        """
    def show_players(self):
        """Affiche la liste de joueurs"""
        print("Liste des joueurs:")
        for player in self.players:
            print(f" - {player.first_name} {player.last_name} ({player.national_id})")

    def show_player(self, player: Player):
        """Affiche les détails d'un joueur

        Args:
            player (Player): Le joueur à afficher
        """
        print(f"Nom: {player.first_name} {player.last_name}")
        print(f"Identifiant national: {player.national_id}")
        print(f"Date de naissance: {player.birth_date}")

    def show_create_player(self):
        """Affiche le formulaire de création de joueur"""
        print("Création d'un joueur")
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        national_id = input("Identifiant national: ")
        birth_date = input("Date de naissance (jj/mm/aaaa): ")
        player = Player(first_name, last_name, national_id, birth_date)
        #return Player(first_name, last_name, national_id, birth_date)
        return player
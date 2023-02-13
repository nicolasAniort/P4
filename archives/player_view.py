from typing import List
from models.player import Player

class PlayerView:
    
    """initialisation du constructeur"""

    def __init__(self, players: List[Player]):
        self.players = players

        """Affiche la liste de joueurs"""   
    def show_players(self):
    
        print("Liste des joueurs:")
        for player in self.players:
            return f" - ({player.last_name} {player.first_name} {player.birth_date} {player.national_id} {player.score})"
             
    def show_player(self, player: Player):
        """
        Affiche les détails d'un joueur
        Args: player (Player): Le joueur à afficher
        """
        print(f"Nom et prénom : {player.first_name} {player.last_name}")
        print(f"Identifiant national: {player.national_id}")
        print(f"Date de naissance: {player.birth_date}")
        #print(f"score: {player.score}")

    def show_create_player(self):
        """Affiche le formulaire de création de joueur"""
        print("---------------------------------------------------------------------|")
        print("Création d'un joueur")
        print("---------------------------------------------------------------------|")
        
        last_name = input("Nom de famille: ")
        first_name = input("Prénom: ")
        national_id = input("Identifiant national: ")
        birth_date = input("Date de naissance (jj/mm/aaaa): ")
        player = Player(last_name, first_name, national_id, birth_date, score = 0)
        return player
import datetime
from typing import List
from models.player import Player
from views.player_view import PlayerView

class PlayerController:
    """initialisation de la liste de joueur"""
    def __init__(self, players = []):
        self.players = players
     
    """Ajout d'un joueur à la liste """
    def add_player(self, player: Player):
        self.players.append(player)
    
    """supprime un joueur de la liste en utilisant une compréhension de liste 
    pour filtrer les joueurs qui ont un ID différent de celui spécifié."""
    def remove(self, id: int):
        self.players = [p for p in self.players if p.id != id]
    
    """generation de la liste de joueur"""        
    def generate_players_list(self):
        players_list = []
        for player in self.players:
            players_list.append(str(player))
        print("Voici la liste des joueurs", "\n".join(players_list))    
        return "\n".join(players_list)
    
    """Generation de la Liste global des inscrits au club"""
    def generate_global_players_list_tournaments(self):
        pass
    
    """saisie d'un joueur"""
    def get_input(self) -> Player:
        last_name = input("Entrez le nom de famille : ")
        first_name = input("Entrez le prénom : ")
        birth_date_str = input("Entrez la date de naissance (JJ/MM/AAAA) : ")
        birth_date = datetime.datetime.strptime(birth_date_str, "%d/%m/%Y").date()
        national_id = input("Entrez l'identifiant national : ")
        score = 0
        return Player(last_name, first_name, birth_date, national_id, score)
    
    #def list_player(self) -> str:
        return self.player_view.list()

    #def get(self, id: int) -> str:
        return self.player_view.get(id)
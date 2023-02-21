import json
from models.player import Player
class PlayerController():

    def __init__(self):
        pass
    
    """ajouter un joueur en ecrivant dans le fichier json ses informations"""
    def write_player(self):        
        players = []
        try:
            with open('data/player/player_data.json', 'r') as file:
                players = json.load(file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

        new_player = {
            "nom": self.last_name,
            "prenom": self.first_name,
            "date_de_naissance" : self.birth_date,
            "identifiant_national": self.national_id,
            "classement": self.rank
        }
        players.append(new_player)

        with open('data/player/player_data.json', 'w') as file:
            json.dump(players, file)
    
    """liste des joueurs enregistrés dans le fichier json"""
    def list_registred_players(self):
    
        # Charger les données à partir du fichier player_data.json
        player_data = []
        with open("data/player/player_data.json", "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)
        #tri par ordre alphabétique
        player_data_alphabetical = sorted(player_data, key=lambda player: player["nom"])
        return player_data_alphabetical
    
    """Changer le classement d'un joueur dans le fichier json player_data.json"""    
    def change_rank_player(self):
        
        # Charger les données à partir du fichier player_data.json
        with open("data/player/player_data.json", "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)
        # trouver le joueur dont le classement doit être modifié
        for player in player_data:
            player_name = input("Entrez le nom du joueur: ")
            player_firstname = input("Entrez le prénom du joueur: ")    
            if player["nom"] == player_name and player["prenom"] == player_firstname:
                player["classement"] = str(int(input("Entrez le nouveau classement: ")))
                break
            else:
                print("Le joueur n'existe pas")

        # Écrire les données modifiées dans le fichier player_data.json
        try:
            player_data_string = json.dumps(player_data, indent=2)
            with open("data/player/player_data.json", "w") as file:
                file.write(player_data_string)
        except json.JSONDecodeError:
            print("Le fichier de données des joueurs est corrompu.")
            return None
    
    """Chercher un joueur dans le fichier json à partir de son identifiant nationnal ses informations"""
    def search_player(self, search_criteria):
        players = []
        try:
            with open('data/player/player_data.json', 'r') as file:
                players = json.load(file)
        except FileNotFoundError:
            print("Aucun joueur n'a été trouvé.")
            return None
        except json.JSONDecodeError:
            print("Le fichier de données des joueurs est corrompu.")
            return None

        for player in players:
            if player["identifiant_national"] == search_criteria :
                print("le joueur existe déjà dans notre base données")
                return player
            
        print("Aucun joueur n'a été trouvé avec les critères de recherche '{}'".format(search_criteria))
        return None
    "lire la fiche d'un joueur dans le fichier json"
    
    def reader_player(national_id):
        national_id_search = national_id
        # Charger les données à partir du fichier player_data.json
        with open("data/player/player_data.json", "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)
        # trouver le joueur dont le classement doit être modifié
        player_for_tournament= Player()
        for player in player_data:
               
            if player["identifiant_national"] == national_id_search:
                player_for_tournament = player["nom"]
                player_for_tournament.first_name = player["prenom"]
                player_for_tournament.birth_date = player["date_de_naissance"]
                player_for_tournament.national_id = player["identifiant_national"]
                player_for_tournament.rank = player["classement"]
                return player_for_tournament

            else:
                print("Le joueur n'existe pas")
                return False
                

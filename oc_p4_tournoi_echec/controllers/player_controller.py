import json
class PlayerController():

    def __init__(self):
        pass
    
    """ajouter un joueur en ecrivant dans le fichier json ses informations"""
    def write_player(self):
        
        players = []
        try:
            with open('data/player_data.json', 'r') as file:
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

        with open('data/player_data.json', 'w') as file:
            json.dump(players, file)
        
    def change_rank_player(self):
        # Charger les données à partir du fichier player_data.json
        with open("data/player_data.json", "r") as file:
            player_data = json.load(file)

        # trouver le joueur dont le classement doit être modifié
        player_name = input("Entrez le nom du joueur: ")
        player_firstname = input("Entrez le prénom du joueur: ")
        for player in player_data:
            if player["nom"] == player_name and player["prenom"] == player_firstname:
                player["classement"] = int(input("Entrez le nouveau classement: "))
                break

        # Écrire les données modifiées dans le fichier player_data.json
        try:
            with open("data/player_data.json", "w") as file:
                json.dump(player_data, file, indent=2)
        except json.JSONDecodeError:
            print("Le fichier de données des joueurs est corrompu.")
            return None
    
    def search_player(self, search_criteria):
        players = []
        try:
            with open('data/player_data.json', 'r') as file:
                players = json.load(file)
        except FileNotFoundError:
            print("Aucun joueur n'a été trouvé.")
            return None
        except json.JSONDecodeError:
            print("Le fichier de données des joueurs est corrompu.")
            return None

        for player in players:
            if player["nom"] == search_criteria["nom"] and player["prenom"] == search_criteria["prenom"]:
                return player
        print("Aucun joueur n'a été trouvé avec les critères de recherche '{}'".format(search_criteria))
        return None
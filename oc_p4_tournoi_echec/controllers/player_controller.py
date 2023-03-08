import re
import json
from models.player import Player
from views.player_view import PlayerView
from views.menuview import Menu

class PlayerController():

    def __init__(self):
        pass
    
    def write_player(self):        
        """ajouter un joueur en ecrivant dans le fichier json ses informations"""
        players = []
        PlayerView.show_create_player(self)
        """ouvrir le fichier json"""
        try:
            with open('data/player/player_data.json', 'r') as file:
                players = json.load(file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
        while True:
            try:
                # Ouvrir le fichier JSON et le lire dans une variable
                with open('data/player/player_data.json', 'r') as file:
                    data = json.load(file)
                national_id = PlayerView.input_national_id(self)                
                if not re.match(r"[A-Za-z]{2}\d{5}", national_id):
                    raise ValueError(PlayerView.error_national_id(self))
                # Rechercher l'identifiant national dans les données
                found = False
                for player in data:
                    if player['identifiant_national'] == national_id:
                        found = True
                        break
                # Afficher un message si l'identifiant a été trouvé ou non
                if found:
                    print("L'identifiant a été trouvé dans les données.")
                    menu = Menu()
                    menu.display_players_menu()
                else:
                    break    
                break
            except ValueError as e:
                print(e)
            try:
                pass
            except ValueError as e:
                print(e)
        while True:
            try:
                last_name = str(PlayerView.input_last_name(self))
                break
            except ValueError:
                PlayerView.error_last_name(self)
        while True:
            try:
                first_name = str(PlayerView.input_first_name(self))
                break
            except ValueError:
                PlayerView.error_first_name(self)            
        while True:
            try:
                birth_date = PlayerView.input_birthday(self)
                if not re.match(r"\d{2}/\d{2}/\d{4}", birth_date):
                    raise ValueError(PlayerView.error_birthday(self))
                break     
            except ValueError as e:
                print(e)
   
        while True:
            try:
                rank = int("0")
                break
            except ValueError:
                print("Veuillez entrer un nom valide")
                
        player: Player = Player(last_name, first_name, birth_date, national_id, rank)
            
        new_player = {
            "nom": player.last_name,
            "prenom": player.first_name,
            "date_de_naissance" : player.birth_date,
            "identifiant_national": player.national_id,
            "classement": player.rank
        }
        players.append(new_player)

        with open('data/player/player_data.json', 'w') as file:
            json.dump(players, file)
    
        PlayerView.show_create_player_ok(self)
                
    def list_registred_players(self):
        """liste des joueurs enregistrés dans le fichier json"""
        # Charger les données à partir du fichier player_data.json
        player_data = []
        with open("data/player/player_data.json", "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)
        #tri par ordre alphabétique
        player_data_alphabetical = sorted(player_data, key=lambda player: player["nom"])
        # trouver la taille maximale pour le nom et le prénom
        longest_name_len = max(len(player["nom"]) for player in player_data)
        longest_firstname_len = max(len(player["prenom"])for player in player_data)
        PlayerView.list_players_view(self, player_data_alphabetical, longest_name_len, longest_firstname_len)
        #return player_data_alphabetical    
    
    def list_players_by_rank(self):
        """liste des joueurs enregistrés dans le fichier json"""
        # Charger les données à partir du fichier player_data.json
        player_data = []
        with open("data/player/player_data.json", "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)
        #tri par ordre alphabétique
        player_data_rank = sorted(player_data, key=lambda player: player["classement"])
        # trouver la taille maximale pour le nom et le prénom
        longest_name_len = max(len(player["nom"]) for player in player_data)
        longest_firstname_len = max(len(player["prenom"])for player in player_data)
        PlayerView.list_players_view(self, player_data_rank, longest_name_len, longest_firstname_len)
        #return player_data_by_rank    
        
        
    """Changer le classement d'un joueur dans le fichier json player_data.json"""    
    def change_rank_player(self):
        PlayerView.display_change_rank_introduce(self)
        player_data = []
        # Charger les données à partir du fichier player_data.json
        with open("data/player/player_data.json", "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)
        
        player_name = PlayerView.input_last_name(self)
        player_firstname = PlayerView.input_first_name(self)     
        # trouver le joueur dont le classement doit être modifié
        for player in player_data:   
            if player["nom"] == player_name and player["prenom"] == player_firstname:
                a = 0
                while a < 1:
                    try:
                        player["classement"] = PlayerView.change_rank(self)
                        PlayerView.display_change_rank_ok(self)
                        a = 1
                        #break
                    except ValueError:
                        print("Erreur de frappe, Veuillez renouveller votre frappe au format numérique: ")
                        

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
            else:
                None
        print("Aucun joueur n'a été trouvé avec les critères de recherche '{}'".format(search_criteria))
        return None    
    """lire la fiche d'un joueur dans le fichier json"""
    def reader_player(self, national_id):
        national_id_search = national_id
        # Charger les données à partir du fichier player_data.json
        with open("data/player/player_data.json", "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)
        # trouver le joueur dont le classement doit être modifié
        player_for_tournament = Player
        for player in player_data:
               
            if player["identifiant_national"] == national_id_search:
                player_for_tournament.last_name = player["nom"]
                player_for_tournament.first_name = player["prenom"]
                player_for_tournament.birth_date = player["date_de_naissance"]
                player_for_tournament.national_id = player["identifiant_national"]
                player_for_tournament.rank = player["classement"]
                return player_for_tournament

            else:
                PlayerView.display_player_not_exist(self)
                return False
        
                    

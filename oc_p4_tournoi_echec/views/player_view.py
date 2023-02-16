import re
import json
from models.player import Player 
from controllers.player_controller import PlayerController
from views.menuview import Menu

class PlayerView():
    
    """ initialisation du constructeur de joueur"""
    def __init__(self):
        pass        
    
    
    """Affiche le formulaire de création de joueur et l'enregistre dans la base de données"""
    def show_create_player(self):
        
        print("---------------------------------------------------------------------|")
        print("-----------------------Création d'un joueur--------------------------|")
        print("---------------------------------------------------------------------|")
        while True:
            try:
                # Ouvrir le fichier JSON et le lire dans une variable
                with open('data/player/player_data.json', 'r') as file:
                    data = json.load(file)
                national_id = input("Identifiant national: ")
                if not re.match(r"[A-Za-z]{2}\d{5}", national_id):
                    raise ValueError("L'identifiant national doit contenir deux lettres et cinq chiffres")
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
                last_name = str(input("Nom de famille: "))
                break
            except ValueError:
                print("Veuillez entrer un nom valide")

        while True:
            try:
                first_name = str(input("Prénom: "))
                break
            except ValueError:
                print("Veuillez entrer un prénom valide")
            
        while True:
            try:
                birth_date = input("Date de naissance (jj/mm/aaaa): ")
                if not re.match(r"\d{2}/\d{2}/\d{4}", birth_date):
                    raise ValueError("La date de naissance doit être au format jj/mm/aaaa")
                break     
            except ValueError as e:
                print(e)
   
        while True:
            try:
                rank = 0
                break
            except ValueError:
                print("Veuillez entrer un nom valide")
                
        player: Player = Player(last_name, first_name, birth_date, national_id, rank)
        player_creation = PlayerController.write_player(player)
        return player_creation
        
    def update_rank(self):
        
        print("---------------------------------------------------------------------|")
        print("-------------Mise à jour du classement du joueur---------------------|")
        print("---------------------------------------------------------------------|")
        print("Entrez les informations de recherche du joueur")
        new_search_player = PlayerController.change_rank_player(self)
        print(f"le classement du joueur a été modifié avec succès")
    
    def list_players_view(self):
        
        player_list = PlayerController.list_registred_players(self)       
        #tri par ordre alphabétique
        player_data_alphabetical = sorted(player_list, key=lambda player: player["nom"])
        
        # trouver le joueur dont le classement doit être modifié
        longest_name_len = max(len(player["nom"]) for player in player_list)
        longest_firstname_len = max(len(player["prenom"])for player in player_list)
        
        # Afficher l'en-tête de la table
        header = "| {:<{}} | {:<{}} | {:<6} | {:<8} | {:<3} |".format("Nom", longest_name_len, "Prénom", longest_firstname_len, "ID national", "date_de_naissance","classement")
        separator = "|" + "-" * (longest_name_len + longest_firstname_len + 52) + "|"
        print("")
        print(separator)
        print(header)
        print(separator)

        # Afficher les données
        for row in player_data_alphabetical:
            line = "| {:<{}} | {:<{}} | {:<11} | {:<17} | {:<10} |".format(row["nom"], longest_name_len, row["prenom"], longest_firstname_len, row["date_de_naissance"], row["identifiant_national"], row["classement"])
            print(line)

        print(separator)
        print("")
    
          
    def display_list_tournament_player():
        pass
    
    def display_player_register(self):
        print("Le joueur a bien été créé et ajouté dans la base de données")

    def display_enter_player_ranking(self, index: str ):
        print("Entrer le nouveau classement du joueur, identifiant national N° : " + str(index))
    
    def display_player_score_updated(self, index: str):
        print("Le joueur , dont l'identifiant national " + str(index) + "la bien été mis à jour")

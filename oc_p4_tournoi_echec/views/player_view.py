import re
import json
from models.player import Player 
#from controllers.player_controller import PlayerController
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
              
    def input_national_id(self):          
        input_id = input("Identifiant national: ")
        return input_id
    def error_national_id(self):
        print("L'identifiant national doit contenir deux lettres et cinq chiffres")
    def input_last_name(self):          
        input_id = input("Nom de famille: ")
        return input_id
    def error_last_name(self):
        print("Veuillez entrer un nom valide")    
    def input_first_name(self):          
        input_id = input("Prénom: ")
        return input_id
    def error_first_name(self):
        print("Veuillez entrer un prénom valide")
    def input_birthday(self):          
        input_id = input("Date de naissance (jj/mm/aaaa): ")
        return input_id
    def error_birthday(self):
        print("La date de naissance doit être au format jj/mm/aaaa")
    def change_rank(self):          
        new_rank = str(int(input("Entrez le nouveau classement: ")))
        return new_rank

    def show_create_player_ok(self): 
        print(" La saisie du joueur a été enregistrée dans la base de données")           
        
    def display_change_rank_introduce(self):
        print("---------------------------------------------------------------------|")
        print("-------------Mise à jour du classement du joueur---------------------|")
        print("---------------------------------------------------------------------|")
        print("Entrez les informations de recherche du joueur")
        
    def display_change_rank_ok(self):
        print(f"le classement du joueur a été modifié avec succès")
    
    def list_players_view(self,player_by_alphabetic,longest_name, longest_firstname):
        
        #tri par ordre alphabétique
        player_data_alphabetical = player_by_alphabetic      
        
        # trouver la taille maximale pour le nom et le prénom
        longest_name_len = longest_name
        longest_firstname_len = longest_firstname
        
        # Afficher l'en-tête de la table
        header = "| {:<{}} | {:<{}} | {:<6} | {:<8} | {:<3} |".format("Nom", longest_name_len, "Prénom", longest_firstname_len, "ID national", "date_de_naissance","classement")
        separator = "|" + "-" * (longest_name_len + longest_firstname_len + 52) + "|"
        print("")
        print(separator)
        print(header)
        print(separator)

        # Afficher les données
        for row in player_data_alphabetical:
            line = "| {:<{}} | {:<{}} | {:<11} | {:<17} | {:<10} |".format(row["nom"], longest_name_len, row["prenom"], longest_firstname_len, row["identifiant_national"], row["date_de_naissance"], row["classement"])
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
   
    def display_player_not_exist(self):
        print("Le joueur n'existe pas.")

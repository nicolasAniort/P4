import json
from models.tournament import Tournament
from models.player import Player

class TournamentView():

    """ initialisation du constructeur de la vue tournoi"""
    def __init__(self):
        pass        
    
    """Affiche le formulaire de création du tournoi et l'enregistre dans la base de données"""
    def show_create_tournament(self):
        
        print("---------------------------------------------------------------------|")
        print("-----------------Création d'un tournoi-------------------------------|")
        print("---------------------------------------------------------------------|")    
        list_input_players = ["", "", "", "", ""]
        list_input_players[0] = input("Nom du tournoi: ")
        list_input_players[1] = input("Lieu: ")
        list_input_players[2] = input("Date de debut: ")
        list_input_players[3] = input("Date de fin: ")
        list_input_players[4] = input("Remarque générales du directeur du tournoi: ")
        return list_input_players
        
    def display_tournament_created(self):
        print("Le tournoi a bien été créé dans la base de données")

    def display_tournament_start(self):
        print("Lancement du nouveau tournoi")
        
    def display_enter_tournament(self):
        print("Entrer le numero du tournoi que l'on souhaite selectionner")
        
    def display_tournament_end(self):
        print("La fin du tournoi est annoncée")
   
          
    """Affiche la liste des tournois dans la base de données"""
    def list_tournaments_view(self):
        tournament_list = TournamentController.list_registred_tournaments(self)       
        #tri par ordre du plus ancien au plus
        tournament_data_alphabetical = sorted(tournament_list, reverse=True, key=lambda tournament: tournament["date_de_debut"])
        # trouver le joueur dont le classement doit être modifié
        longest_name_len = max(len(tournament["nom_du_tournoi"]) for tournament in tournament_list)
        longest_firstname_len = max(len(tournament["lieu"])for tournament in tournament_list)
        # Afficher l'en-tête de la table
        header = "| {:<{}} | {:<{}} | {:<6} | {:<8} | {:<3} |".format("Nom du tournoi", longest_name_len, "Lieu", longest_firstname_len, "Date de début", "Date de fin","Nombre de round", "Description du tournoi","Numero du round en cour", "Listes de rounds", "Liste des joueurs")

        separator = "|" + "-" * (longest_name_len + longest_firstname_len + 53) + "|"
        print("")
        print(separator)
        print(header)
        print(separator)
        # Afficher les données
        for row in tournament_data_alphabetical:
            line = "| {:<{}} | {:<{}} | {:<13} | {:<11} | {:<15} |".format(row["nom_du_tournoi"], longest_name_len, row["lieu"], longest_firstname_len, row["date_de_debut"], row["date_de_fin"], row["nombre_de_round"], row["description_tournoi"],row["numero_round_actif"],row["liste_des_rounds"],row["liste_des_joueurs"])
            print(line)

        print(separator)
        print("")
    
    """Affiche la liste des tournois """
    def list_tournaments_for_choice_view(self, tournament_list):         
        # Affichage de la liste des tournois avec leur numéro d'index
        print("")
        for index, tournament in enumerate(tournament_list):
            print(f"{index}: {tournament['nom_du_tournoi']},{tournament['date_de_debut']}")
        print("")
    
    def display_choice_tournament(self):
        index_selected = int(input("Sélectionnez un tournoi en entrant son numéro: "))
        return index_selected
        
    """Affiche le formulaire d'ajout d'un joueur au tournoi actif"""
    def display_add_player_to_tournament(self):    
        print("---------------------------------------------------------------------|")
        print("-----------------Ajouter un joueur au tournoi------------------------|")
        print("---------------------------------------------------------------------|")      
        national_id_new = str(input("Saisir l'identifiant nation du joueur: "))
        return national_id_new
                           
    def create_rounds(self):
        pass
    
    def display_tournament_register(self):
        print("Le tournoi a bien été créé et ajouté dans la base de données")

    def display_enter_player(self, index: str ):
        print("Entrer le nouveau classement du joueur, identifiant national N° : " + str(index))
    
    def display_player_score_updated(self, index: str):

        print("Le joueur , dont l'identifiant national " + str(index) + "la bien été mis à jour")

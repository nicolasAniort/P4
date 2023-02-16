from models.tournament import Tournament
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController

class TournamentView():

    """ initialisation du constructeur de la vue tournoi"""
    def __init__(self):
        pass        
    """Affiche le formulaire de création du tournoi et l'enregistre dans la base de données"""
    def show_create_tournament(self):
        
        print("---------------------------------------------------------------------|")
        print("-----------------Création d'un tournoi-------------------------------|")
        print("---------------------------------------------------------------------|")    
        tournament_name = input("Nom du tournoi: ")
        tournament_location = input("Lieu: ")
        tournament_date_start = input("Date de debut: ")
        tournament_date_end = input("Date de fin: ")
        tournament_description = input("Remarque générales du directeur du tournoi: ")
        tournament_number_of_round = 4
        tournament_round_number = 1
        tournament_round_list = []
        tournament_players_list: str = ""
        tournament: Tournament = Tournament(tournament_name,tournament_location,tournament_date_start,tournament_date_end,tournament_number_of_round,tournament_description,tournament_round_number,tournament_round_list,tournament_players_list)
        tournament_creation = TournamentController.write_tournament(tournament)
        return tournament_creation
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
    """Affiche la liste des choix de tournois """
    def list_tournaments_for_choice_view(self):
        tournament_list = TournamentController.list_tournament_for_choice(self)       
        # Affichage de la liste des tournois avec leur numéro d'index
        print("")
        for index, tournament in enumerate(tournament_list):
            print(f"{index}: {tournament['nom_du_tournoi']},{tournament['date_de_debut']}")
        print("")
        # Demande à l'utilisateur de choisir un tournoi
        selected_index = int(input("Sélectionnez un tournoi en entrant son numéro: "))

        # Accès au tournoi sélectionné
        selected_tournament = tournament_list[selected_index]
        return selected_tournament
    """Affiche le formulaire d'ajout d'un joueur au tournoi actif"""
    def add_player_to_tournament(self, tournament: Tournament):    
        print("---------------------------------------------------------------------|")
        print("-----------------Ajouter un joueur au tournoi------------------------|")
        print("---------------------------------------------------------------------|")
        tournament_active: Tournament = tournament
        national_id_new = str(input("Saisir l'identifiant nation du joueur: "))
        player_new = PlayerController()
        if player_new.search_player(search_criteria=national_id_new)== True:
            
            print("Le joueur existe déjà, donc je vais ecrire juste ID dans la base de données du tournoi")
        else:
            print("Enregistrement du nouveau joueur , enregistrement de player_data.json , et enregitsreement de son id_national dans tournament_data.json")
                      
    def create_rounds(self):
        pass
    
    def display_tournament_register(self):
        print("Le tournoi a bien été créé et ajouté dans la base de données")

    def display_enter_player(self, index: str ):
        print("Entrer le nouveau classement du joueur, identifiant national N° : " + str(index))
    
    def display_player_score_updated(self, index: str):

        print("Le joueur , dont l'identifiant national " + str(index) + "la bien été mis à jour")

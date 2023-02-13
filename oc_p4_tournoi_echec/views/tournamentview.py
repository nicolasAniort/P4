from models.tournament import Tournament
from controllers.tournament_controller import TournamentController
class TournamentView():

    """ initialisation du constructeur de joueur"""
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
        tournament_players_list = []
        tournament_number_of_round :int = len(tournament_players_list)
        if tournament_number_of_round < 4:
            tournament_number_of_round = 4
        else:
                tournament_number_of_round
        tournament_description = input("Remarque générales du directeur du tournoi: ")
        tournament_round_number = 1
        tournament_round_list = []
        tournament: Tournament = Tournament(tournament_name,tournament_location,tournament_date_start,tournament_date_end,tournament_number_of_round,tournament_description,tournament_round_number,tournament_round_list,tournament_players_list)
        tournament_creation = TournamentController.write_tournament(tournament)
        return tournament_creation
    
    def select_tournament(self):
        print("---------------------------------------------------------------------|")
        print("----------------------Selectionner un tournoi------------------------|")
        print("---------------------------------------------------------------------|")
        
        pass
    
    def add_player_to_tournament(self, tournament: Tournament):

        print("---------------------------------------------------------------------|")
        print("-----------------Ajouter un joueur au tournoi------------------------|")
        print("---------------------------------------------------------------------|")
        number_player = len(tournament.players_list)
        print(f"Nombre de joueurs: {number_player}")
      
    def create_rounds(self):
        pass
    
    def display_tournament_register(self):
        print("Le tournoi a bien été créé et ajouté dans la base de données")

    def display_enter_player(self, index: str ):
        print("Entrer le nouveau classement du joueur, identifiant national N° : " + str(index))
    
    def display_player_score_updated(self, index: str):

        print("Le joueur , dont l'identifiant national " + str(index) + "la bien été mis à jour")

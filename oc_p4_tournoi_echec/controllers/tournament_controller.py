import re
import json
class TournamentController():

    def __init__(self):
        pass
    
    def create_tournament(self):
        """Creer un nouveau tournoi """
        tournaments = []
        try:
            with open('data/tournaments/tournament_data.json', 'r') as file:
                tournaments = json.load(file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
        new_tournament_name = self.tournament_name
        new_tournament_date_start = self.tournament_date_start
        new_tournament = {
            
        "nom_du_tournoi":self.tournament_name,
        "lieu":self.tournament_location,
        "date_de_debut":self.tournament_date_start,
        "date_de_fin":self.tournament_date_end,
        "nombre_de_round":self.tournament_number_of_round,
        "description_tournoi":self.tournament_description,
        "numero_round_actif":self.tournament_round_number,
        "liste_des_rounds":self.tournament_round_list,
        "liste_des_joueurs":TournamentController.create_file_player_path(tournament_name = new_tournament_name,tournament_date_start = new_tournament_date_start)      
        }
        tournaments.append(new_tournament)

        with open('data/tournaments/tournament_data.json', 'w') as file:
            json.dump(tournaments, file)
        
        tournament_players = []    
        new_tournament_players_file = {
            "identifiant_nationnal": '',
            "nom_du_joueur" : '',
            "prenom": '',
            "classsement" : ''            
        }
        tournament_players.append(new_tournament_players_file)
        file_path = TournamentController.create_file_player_path(new_tournament_name,new_tournament_date_start)

        with open(file_path, 'x') as file:
            json.dump(tournament_players, file)     
        
    def list_registred_tournaments(self):
        """Liste des tournois classés par ordre alphabétique"""
        # Charger les données à partir du fichier tournament_data.json
        tournament_data = []
        with open("data/tournaments/tournament_data.json", "r") as file:
            file_contents = file.read()
            tournament_data = json.loads(file_contents)
        #tri par ordre alphabétique
        tournament_data_alphabetical = sorted(tournament_data, key=lambda tournament: tournament["nom_du_tournoi"])
        return tournament_data_alphabetical
    
    """Liste des tournois classés par date"""
    def list_tournament_for_choice(self):
        # Charger les données à partir du fichier tournament_data.json
        tournament_data = []
        with open("data/tournaments/tournament_data.json", "r") as file:
            file_contents = file.read()
            tournament_data = json.loads(file_contents)
        #tri par ordre d'ancienneté
        tournament_data_date = sorted(tournament_data, reverse=True, key=lambda tournament: tournament["nom_du_tournoi"])
        return tournament_data_date
    
    """methode de creation du chemin d'accès au fichier du nouveau tournoi"""
    def create_file_player_path(tournament_name,tournament_date_start):    
        
        date_string = tournament_date_start
        date_string = re.sub("\/","",date_string)
        name_string = tournament_name
        name_string = re.sub("\ ", "_", name_string)
        file_name = str( name_string + date_string + ".json")
        file_path = 'data/tournaments/' + file_name
        return file_path
        
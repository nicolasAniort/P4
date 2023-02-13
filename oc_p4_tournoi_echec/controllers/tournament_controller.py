import json
class TournamentController():

    def __init__(self):
        pass
    """ajouter un joueur en ecrivant dans le fichier json ses informations"""
    def write_tournament(self):
        
        tournaments = []
        try:
            with open('data/tournament_data.json', 'r') as file:
                tournaments = json.load(file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

        new_tournament = {
            
        "nom_du_tournoi":self.tournament_name,
        "lieu":self.tournament_location,
        "date_de_debut":self.tournament_date_start,
        "date_de_fin":self.tournament_date_end,
        "nombre_de_round":self.tournament_number_of_round,
        "description_tournoi":self.tournament_description,
        "numero_round_actif":self.tournament_round_number,
        "liste_des_rounds":self.tournament_round_list,
        "liste_des_joueurs":self.tournament_players_list      
        }
        tournaments.append(new_tournament)

        with open('data/tournament_data.json', 'w') as file:
            json.dump(tournaments, file)
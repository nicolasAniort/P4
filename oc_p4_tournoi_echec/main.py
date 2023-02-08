import argparse
import json
import os
from views.tournament_view import TournamentView
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from models.tournament import Tournament

filepath_tournament = str("C:/Users/conta/OneDrive/PROJETS_DEV/1-OC_PYTHON/PROJ4/DEV/PROJ4/oc_p4_tournoi_echec/data/tournaments/files.json")


def save_tournament(filepath_tournament, tournament):
    """
    Sauvegarde un tournoi dans un fichier JSON
    :param filepath: Chemin vers le fichier JSON où sauvegarder
    :param tournament: Objet Tournament à sauvegarder
    """
    with open(filepath_tournament, "a+") as f:
        f.write(tournament.to_json())

def main():
    # On utilise argparse pour récupérer les arguments passés en ligne de commande
    parser = argparse.ArgumentParser()
    parser.add_argument('--load', type=str, help='Chemin vers le fichier JSON à charger')
    parser.add_argument('--save', type=str, help='Chemin vers le fichier JSON où sauvegarder')
    args = parser.parse_args()

    if args.load:
        tournament = TournamentController.load_tournament(args.load) 
    else:
        tournament = TournamentController.load_tournament(filepath_tournament)
        
    player_controller = PlayerController(players = [])
    # Si le tournoi n'est pas chargé, on demande à l'utilisateur de saisir les informations nécessaires
    if tournament is None:
        controller = TournamentController(player_controller.players)
          

    # On instancie le contrôleur et la vue
    
    view = TournamentView(tournament)
    
    while True:
        # Affichage du menu principal
        view.display_menu()
        choice = view.get_input()

        # Si l'utilisateur choisit de quitter, on sauvegarde le tournoi et on quitte la boucle
        if choice == 'q':
            save_tournament(args.save, tournament)
            break
        else:
           
        # Sinon, on appelle la méthode du contrôleur correspondant au choix de l'utilisateur
            controller = TournamentController(players = [])
            getattr(controller, choice)()

if __name__ == "__main__":
    main()        

import argparse
import json
import os
from views.tournament_view import TournamentView
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from models.tournament import Tournament
from models.player import Player

filepath = str("/data/players/file.json")

def load_tournament(filepath):
    """
    Charge un tournoi à partir d'un fichier JSON
    :param filepath: Chemin vers le fichier JSON à charger
    :return: Un objet Tournament ou None si le fichier est vide ou ne contient pas de données valides
    """
    print(filepath)
    if not os.path.isfile(filepath):
        open(filepath, 'w').close()
    try:
        with open(filepath, 'r') as f:
            json_data = json.load(f)
        tournament = Tournament.from_json(json_data)
    except json.decoder.JSONDecodeError:
        tournament = None
    return tournament


def save_tournament(filepath, tournament):
    """
    Sauvegarde un tournoi dans un fichier JSON
    :param filepath: Chemin vers le fichier JSON où sauvegarder
    :param tournament: Objet Tournament à sauvegarder
    """
    if tournament:
        tournament.to_json(filepath)

def main():
    # On utilise argparse pour récupérer les arguments passés en ligne de commande
    parser = argparse.ArgumentParser()
    parser.add_argument('--load', type=str, help='Chemin vers le fichier JSON à charger')
    parser.add_argument('--save', type=str, help='Chemin vers le fichier JSON où sauvegarder')
    args = parser.parse_args()

    tournament = load_tournament(args.load) 
    #if args.load
    #else: 
    #    None
        
    player_controller = PlayerController(players = [])
    # Si le tournoi n'est pas chargé, on demande à l'utilisateur de saisir les informations nécessaires
    if tournament is None:
        controller = TournamentController(tournament = tournament, players = player_controller.players)
    else:
        controller = TournamentController(tournament = None, players = player_controller.players)
         

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
        # Sinon, on appelle la méthode du contrôleur correspondant au choix de l'utilisateur
           # if choice in switcher:
           #     switcher[choice]()
           # else:
           #     print("Invalid option")
        # Sinon, on appelle la méthode du contrôleur correspondant au choix de l'utilisateur
        getattr(controller, choice)()

if __name__ == "__main__":
    main()        

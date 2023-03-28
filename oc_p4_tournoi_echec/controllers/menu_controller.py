from views.menuview import Menu
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.round_controller import RoundController


class MenuController:
    def __init__(self):
        self.menu = Menu()
        self.playercontroller = PlayerController()
        self.tournamentcontroller = TournamentController()
        self.roundcontroller = RoundController()

    def confirm_quit(self):
        confirm_choice = Menu.choice_to_quit(self)
        if confirm_choice == "0":
            exit()
        else:
            self.main_menu()

    def main_menu(self):
        x = 0
        while x < 1:
            self.menu.display_main_menu()
            nb_choice = self.menu.choice()

            match str(nb_choice):
                case "1":
                    """acces au sous menu joueur"""
                    y = 0
                    while y < 1:
                        self.menu.display_players_menu()
                        nb_choice = self.menu.choice()
                        match str(nb_choice):
                            case "11":
                                fpath = "data/player/player_data.json"
                                new_user = self.playercontroller.write_player(
                                    path=fpath
                                )
                                self.playercontroller.update_file_players(
                                    players=new_user, file_path=fpath
                                )
                                y = 0
                                # self.main_menu()

                            case "12":
                                self.playercontroller.change_rank_player()
                                # self.menu.display_players_menu()
                                y = 0
                                # self.main_menu()

                            case "13":
                                # self.main_menu()
                                y = 1
                case "2":
                    """acces au sous menu tournois"""
                    z = 0
                    while z < 1:
                        self.menu.display_tournaments_menu()
                        nb_choice = self.menu.choice()
                        match str(nb_choice):
                            case "21":
                                # crééer un tournoi
                                self.tournamentcontroller.create_tournament()
                                z = 0

                            case "22":
                                # Selectionner un tournoi
                                tournament_choice = (
                                    self.tournamentcontroller.list_tournament_choice()
                                )
                                print(
                                    "tournament choisi :",
                                    tournament_choice["nom_du_tournoi"],
                                )
                                sub = 0
                                while sub < 1:
                                    # acces au sous menu tournois
                                    self.menu.display_tournaments_submenu(
                                        tournament_choice
                                    )
                                    nb_choice = self.menu.choice()
                                    match str(nb_choice):
                                        case "221":
                                            # Ajouter un joueur au tournoi
                                            self.tournamentcontroller.add_player_to_tournament(
                                                tournament_choice
                                            )
                                            sub = 0
                                        case "222":
                                            # Générer les tours et les matchs 
                                            # et afficher le tableau
                                            self.roundcontroller.create_round(
                                                tournament_choice
                                            )
                                            sub = 0
                                        case "223":
                                            # mise à jours des scores des 
                                            # matchs du round
                                            self.roundcontroller.update_round(
                                                tournament_choice
                                            )
                                            sub = 0
                                        case "224":
                                            # liste des joueurs triés par
                                            # classement decroissant
                                            self.tournamentcontroller.report_player_by_rank(
                                                tournament_choice
                                            )
                                            sub = 0
                                        case "225":
                                            # liste des joueurs triés par classement decroissant
                                            self.tournamentcontroller.report_player_by_name(
                                                tournament_choice
                                            )
                                            sub = 0
                                        case "229":
                                            # retour au menu supérieur
                                            sub = 1
                                z = 0

                            case "23":
                                z = 1

                case "3":
                    """acces au sous menu rapport"""
                    w = 0
                    while w < 1:
                        self.menu.display_rapport_menu()
                        nb_choice = self.menu.choice()
                        match str(nb_choice):
                            case "31":
                                # affichage des joueurs par ordre alphabetique
                                file_path = "data/player/player_data.json"
                                new_report = PlayerController()
                                new_report.list_registred_players(file_path)
                                w = 0

                            case "32":
                                # affichage des joueurs par score
                                file_path = "data/player/player_data.json"
                                new_repport_rank_player = PlayerController()
                                new_repport_rank_player.list_players_by_rank(
                                    file_path)
                                w = 0

                            case "33":
                                # affichage de tous les tournois
                                new_report_tournament = TournamentController()
                                new_report_tournament.list_saved_tournaments()
                                w = 0

                            case "34":
                                # affichage des joueurs par ordre alphabetique 
                                # et par tours
                                w = 0
                            case "35":
                                # affichage des joueurs par score et par tours
                                w = 0
                            case "36":
                                w = 1

                case "4":
                    self.confirm_quit()

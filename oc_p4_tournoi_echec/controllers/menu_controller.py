from views.menuview import Menu
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.round_controller import RoundController


class MenuController:
    def __init__(self):
        self.menu = Menu()
        self.playercontroller = PlayerController()
        self.tmtcontroller = TournamentController()
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
                    # acces à la creation d'un tournoi
                    self.tmtcontroller.create_tournament()
                    x = 0
                case "2":
                    # Selectionner un tournoi
                    tournament_choice = (
                        self.tmtcontroller
                        .list_tournament_choice()
                    )
                    print(
                        "tournament choisi :",
                        tournament_choice["nom_du_tournoi"]
                    )
                    sub = 0
                    while sub < 1:
                        # acces au sous menu tournois
                        self.menu.display_tournaments_submenu(
                            tournament_choice
                        )
                        nb_choice = self.menu.choice()
                        match str(nb_choice):
                            case "21":
                                # Ajouter un joueur au tournoi
                                self.tmtcontroller.add_player_to_tournament(
                                    tournament_choice
                                    )
                                sub = 0
                            case "22":
                                # Générer les tours et les matchs
                                # et afficher le tableau
                                self.roundcontroller.create_round(
                                    tournament_choice
                                )
                                sub = 0
                            case "23":
                                # mise à jours des scores des
                                # matchs du round
                                self.roundcontroller.update_round(
                                    tournament_choice
                                )
                                sub = 0
                            case "24":
                                # liste des joueurs triés par
                                # classement decroissant
                                self.tmtcontroller.report_player_by_rank(
                                    tournament_choice
                                )
                                sub = 0
                            case "25":
                                # liste des joueurs
                                # triés par classement decroissant
                                self.tmtcontroller.report_player_by_name(
                                    tournament_choice
                                )
                                sub = 0
                            case "26":
                                # liste des tours et des matchs du tours
                                self.roundcontroller.list_rounds(
                                    tournament_choice
                                )
                                sub = 0
                            case "27":
                                # retour au menu supérieur
                                sub = 1
                    x = 0
                case "3":
                    # affichage de tous les tournois
                    new_report_tournament = TournamentController()
                    new_report_tournament.list_saved_tournaments()
                case "4":
                    self.confirm_quit()

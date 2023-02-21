from views.player_view import PlayerView
from views.menuview import Menu
from views.tournamentview import TournamentView
from controllers.player_controller import PlayerController


class MenuController():

    def __init__(self):

        self.menu = Menu()
        
    def confirm_quit(self):
        confirm_choice = input("Si vous souhaitez quitter, tapez 0 : ")
        if confirm_choice == "0":
            exit()
        else:
            self.main_menu()

    def main_menu(self):

        self.menu.display_main_menu()
        nb_choice = self.menu.choice()
           
        match str(nb_choice):
            case "1": 
                """acces au sous menu joueur"""
                self.menu.display_players_menu()
                nb_choice = self.menu.choice()
                match str(nb_choice):
                    case "11": 
                        new_view_player = PlayerView()
                        new_view_player.show_create_player()
                        new_view_player.display_player_register()
                        self.main_menu()
                                              
                    case "12": 
                        new_view_player = PlayerView()
                        new_view_player.update_rank()
                        self.main_menu()
                        
                    case "13": 
                        self.main_menu()
                    
            case "2":
                """acces au sous menu tournois""" 
                self.menu.display_tournaments_menu()
                nb_choice = self.menu.choice()
                match str(nb_choice):
                    case "21": 
                        # crééer un tournoi
                        print("retour dans menu controller apres creation du joueur")
                        new_view_tournement = TournamentView()
                        new_view_tournement.show_create_tournament()
                        new_view_tournement.display_tournament_register()
                        self.main_menu()
                                              
                    case "22": 
                        #Selectionner un tournoi
                        new_view_tournament_open = TournamentView()
                        tournament_choice = new_view_tournament_open.list_tournaments_for_choice_view()
                        print("tournament choisi :", tournament_choice)
                        #acces au sous menu tournois 
                        self.menu.display_tournaments_submenu(tournament_choice)                        
                        nb_choice = self.menu.choice()        
                        match str(nb_choice):
                            case "221":
                                #Ajouter un joueur au tournoi
                                new_view_tournament_open.add_player_to_tournament(tournament_choice)
                                
                            case "222":
                                #Générer les tours et les matchs et afficher le tableau 
                                pass                            
                            case "223":
                                #Saisie des scores
                                pass
                            case "224":
                                #retour au menu supérieur
                                pass
                        print("retour dans menu controller apres modification du classement du joueur")
                        
                    case "23": 
                        self.main_menu()
                    
            case "3": 
                """acces au sous menu rapport"""
                self.menu.display_rapport_menu()
                nb_choice = self.menu.choice()
                match str(nb_choice):
                    case "31": 
                        # affichage des joueurs par ordre alphabetique
                        new_report = PlayerView()
                        new_report.list_players_view() 
                        self.main_menu()
                                              
                    case "32": 
                        # affichage des joueurs par score
                        new_view_player = PlayerView()
                        new_view_player.update_rank()
                        print("retour dans menu controller apres modification du classement du joueur")
                        
                    case "33": 
                        # affichage de tous les tournois
                        new_report_tournament = TournamentView()
                        new_report_tournament.list_tournaments_view() 
                        self.main_menu()
                        
                    case "34": 
                        # affichage des joueurs par ordre alphabetique et par tours
                        pass
                    case "35": 
                        # affichage des joueurs par score et par tours
                        pass
                    case "36": 
                        self.main_menu()

            case "4": 
                self.confirm_quit()
  
    
    
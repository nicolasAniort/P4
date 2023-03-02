from views.player_view import PlayerView
from views.menuview import Menu
from views.tournamentview import TournamentView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController



class MenuController():

    def __init__(self):

        self.menu = Menu()
        
    def confirm_quit(self):
        confirm_choice = Menu.choice_to_quit(self)   
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
                        new_controller_player = PlayerController()
                        new_controller_player.write_player()
                        self.main_menu()
                                              
                    case "12": 
                        new_controller_player = PlayerController()
                        new_controller_player.change_rank_player()
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
                        new_controller_tournement = TournamentController()
                        new_controller_tournement.create_tournament()
                        self.main_menu()
                                              
                    case "22": 
                        #Selectionner un tournoi
                        new_controller_tournament_open = TournamentController()
                        tournament_choice = new_controller_tournament_open.list_tournament_for_choice()
                        print("tournament choisi :", tournament_choice['nom_du_tournoi'])
                        #acces au sous menu tournois 
                        self.menu.display_tournaments_submenu(tournament_choice)                        
                        nb_choice = self.menu.choice()        
                        match str(nb_choice):
                            case "221":
                                #Ajouter un joueur au tournoi
                                new_controller_tournament_open.add_player_to_tournament(tournament_choice)
                                
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
                        new_report = PlayerController()
                        new_report.list_registred_players()
                        self.main_menu()
                                              
                    case "32": 
                        # affichage des joueurs par score
                        new_repport_rank_player = PlayerController()
                        new_repport_rank_player.list_players_by_rank()
                        self.main_menu()
                        
                    case "33": 
                        # affichage de tous les tournois
                        new_report_tournament = TournamentController()
                        new_report_tournament.list_registred_tournaments() 
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
  
    
    
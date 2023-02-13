from models.tournament import Tournament

class TournamentView:
    
    """
    Cette méthode est le constructeur de la classe. 
    Elle est appelée lorsque vous créez une instance de TournamentView.
    Elle prend en argument une variable tournament de type Tournament 
    et la stocke dans l'instance de la classe sous le nom self.tournament.
    """
    
    def __init__(self, tournament: Tournament):
        self.tournament = tournament

    """Cette méthode affiche le menu principal de l'application."""
    def display_menu(self):
        print('Menu principal:')
        print('---------------------------------------------------------------------|')
        print('ACTION SUR LES TOURNOIS                                              |')
        print('---------------------------------------------------------------------|')
        print('1: créer un nouveau tournoi vide                                     |')
        print('2: peupler un tournoi                                                |')
        print("3: gérer un tournoi                                                  |")
        print('---------------------------------------------------------------------|')
        print('RAPPORTS                                                             |')
        print('---------------------------------------------------------------------|')
        print('4: afficher la liste des joueurs par ordre alphabetique              |')
        print('5: afficher la liste des joueurs inscrits                            |')
        print("6: afficher les résultats par tour du tournoi                        |")
        print('7: afficher la liste de tous les tournois                            |')
        print('---------------------------------------------------------------------|')
        print('RAPPORTS                                                             |')
        print('---------------------------------------------------------------------|')
        print("q: quitter l'application                                             |")
        print('---------------------------------------------------------------------|')
 
    """Cette méthode permet de selectionner le choix souhaité dans le sous menu de peuplement d'un tournoi """
    def display_submenufilling(self):
        print('SOUS MENU:')
        print('---------------------------------------------------------------------|')
        print('PEUPLER UN TOURNOI                                                   |')
        print('---------------------------------------------------------------------|')
        print('1: choisir le tournoi                                                |')
        print('2: inscrire les joueurs                                              |')
        print("3: revenir au menu principal                                         |")
        print('---------------------------------------------------------------------|')
        print('---------------------------------------------------------------------|')
        print("q: quitter l'application                                             |")
        print('---------------------------------------------------------------------|')

        """Cette méthode permet de selectionner le choix souhaité dans le sous menu de peuplement d'un tournoi """
    
    def display_managedtournament(self):
        print('SOUS MENU:')
        print('---------------------------------------------------------------------|')
        print('GERER UN TOURNOI                                                     |')
        print('---------------------------------------------------------------------|')
        print('1: choisir le tournoi                                                |')
        print('2: afficher les tours et matchs                                      |')
        print('3: inscrire les scores des matchs                                    |')
        print('4: voir le classement des joueurs                                    |')
        print('5: voir la liste des joueurs par ordre alphabetique                  |')
        print("6: revenir au menu principal                                         |")
        print('---------------------------------------------------------------------|')
        print('---------------------------------------------------------------------|')
        print("q: quitter l'application                                             |")
        print('---------------------------------------------------------------------|')
 
    """Cette méthode permet de selectionner le choix souhaité"""
    def get_input(self):
        choice = input('Entrez votre choix: ')
        return choice 

    """Cette méthode affiche le message "Choix: " et attend une entrée de l'utilisateur, puis renvoie cette entrée sous forme de chaîne de caractères."""
    
    def display_players(self):
        players = self.tournament.players
        print("display_players", players)
        for player in players:
            print(player)

    """ Cette méthode récupère la liste de joueurs de l'instance de Tournament stockée dans self.tournament, puis affiche chaque joueur de la liste."""

    def display_tournaments(self):
        tournaments = self.tournament
        for tournament in tournaments:
            print(tournament)

    """ Cette méthode récupère la liste de tournois de l'instance de Tournament stockée dans self.tournament, puis affiche chaque tournoi de la liste. """

    def display_round_pairs(self, round_number: int):
        pairs = self.tournament.get_round_pairs(round_number)
        for pair in pairs:
            print(f'{pair[0]} vs {pair[1]}')


    """ Cette méthode récupère la liste de paires pour un tour donné de l'instance de Tournament stockée dans self.tournament, puis affiche chaque paire de la liste."""

    def display_round_results(self, round_number: int):
        results = self.tournament.get_round_results(round_number)
        for result in results:
            print(f'{result[0]} vs {result[1]}: {result[2]} - {result[3]}')

        #print('T: afficher la liste des tournois')
        #print('s: sélectionner un tournoi')
        
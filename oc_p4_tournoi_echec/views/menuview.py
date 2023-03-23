from models.tournament import Tournament


class Menu:
    def choice(self):
        while True:
            try:
                number_choice = int(input("Entrez votre choix: "))
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")
        return number_choice

    def display_main_menu(self):
        """l'affichage du menu principal"""
        print("")
        print("---------------------------------------------------------------------|")
        print("---------------------Menu principal----------------------------------|")
        print("---------------------------------------------------------------------|")
        print("1. Joueurs                             ------------------------------|")
        print("2. Tournois                            ------------------------------|")
        print("3. Rapport                             ------------------------------|")
        print("4. Quitter le programme                ------------------------------|")
        print("---------------------------------------------------------------------|")

    def display_players_menu(self):
        """affichage du menu des joueurs"""
        print("")
        print("---------------------------------------------------------------------|")
        print("------------------------Menu joueur----------------------------------|")
        print("---------------------------------------------------------------------|")
        print("11. ajouter un joueur                     ---------------------------|")
        print("12. Mise à jour du classement d'un joueur ---------------------------|")
        print("13. retour au menu principal              ---------------------------|")
        print("---------------------------------------------------------------------|")

    def display_tournaments_menu(self):
        """affichage du menu du tournoi"""
        print("")
        print("---------------------------------------------------------------------|")
        print("------------------------Menu tournoi---------------------------------|")
        print("---------------------------------------------------------------------|")
        print("21. Créer un tournoi                      ---------------------------|")
        print("22. Sélectionner un tournoi               ---------------------------|")
        print("23. retour au menu principal              ---------------------------|")
        print("---------------------------------------------------------------------|")

    def display_tournaments_submenu(self, tournament: Tournament):
        """affichage du menu du tournoi"""
        print("")
        print("---------------------------------------------------------------------|")
        print("----------------Sous-Menu du tournoi---------------------------------|")
        print("---------------------------------------------------------------------|")
        print("221. Ajouter un joueur                                       --------|")
        print("222. Générer les tours et les matchs                         --------|")
        print("223. Saisie des scores                                       --------|")
        print("224. Rapport: liste des joueurs par classement               --------|")
        print("225. Rapport: liste des joueurs par ordre alphabétique       --------|")
        print("229. retour au menu supérieur                                --------|")
        print("---------------------------------------------------------------------|")

    def display_rapport_menu(self):
        """Affichage des rapports"""
        print("")
        print("---------------------------------------------------------------------|")
        print("------------------------Menu rapport---------------------------------|")
        print("---------------------------------------------------------------------|")
        print("31. Affichage des joueurs par ordre alphabétique              -------|")
        print("32. Affichage des joueurs par score                           -------|")
        print("33. Affichage de tous les tournois                            -------|")
        print("34. Affichage des joueurs par ordre alphabétique et par tours -------|")
        print("35. Affichage des joueurs par score et par tours              -------|")
        print("36. retour au menu principal                                  -------|")
        print("---------------------------------------------------------------------|")

    def choice_to_quit(self):
        confirm = input("Si vous souhaitez quitter, tapez 0 : ")
        return confirm

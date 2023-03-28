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
        end_lig1 = "-----------------|"
        
        print("")
        print(f"---------------------Me principal-----------------{ end_lig1}")
        print(f"--------------------------------------------------{ end_lig1}")
        print(f"--------------------------------------------------{ end_lig1}")
        print(f"1. Joueurs                           -------------{ end_lig1}")
        print(f"2. Tournois                          -------------{ end_lig1}")
        print(f"3. Rapport                           -------------{ end_lig1}")
        print(f"4. Quitter le programme                -----------{ end_lig1}")
        print(f"--------------------------------------------------{ end_lig1}")

    def display_players_menu(self):
        """affichage du menu des joueurs"""
        end_lig1 = "-----------------|"
        print("")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"------------------------Menu joueur---------------{end_lig1}")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"11. ajouter un joueur                     --------{end_lig1}")
        print(f"12. Mise à jour du classement d'un joueur --------{end_lig1}")
        print(f"13. retour au menu principal              --------{end_lig1}")
        print(f"--------------------------------------------------{end_lig1}")

    def display_tournaments_menu(self):
        """affichage du menu du tournoi"""
        end_lig1 = "-----------------|"
        print("")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"------------------------Menu tournoi--------------{end_lig1}")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"21. Créer un tournoi                      --------{end_lig1}")
        print(f"22. Sélectionner un tournoi               --------{end_lig1}")
        print(f"23. retour au menu principal              --------{end_lig1}")
        print(f"--------------------------------------------------{end_lig1}")

    def display_tournaments_submenu(self, tournament: Tournament):
        """affichage du menu du tournoi"""
        end_lig1 = "-----------------|"
        end_l2 = "                --------|"
        print("")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"----------------Sous-Menu du tournoi--------------{end_lig1}")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"221. Ajouter un joueur                       {end_l2}")
        print(f"222. Générer les tours et les matchs         {end_l2}")
        print(f"223. Saisie des scores                       {end_l2}")
        print(f"224. Liste des joueurs par classement        {end_l2}")
        print(f"225. Liste des joueurs par ordre alphabétique{end_l2}")
        print(f"229. retour au menu supérieur                {end_l2}")
        print(f"--------------------------------------------------{end_lig1}")

    def display_rapport_menu(self):
        """Affichage des rapports"""
        end_lig1 = "-------------------|"
        end_lig2 = "              -------|"
        print("")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"------------------------Menu rapport--------------{end_lig1}")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"31. Affichage des joueurs par ordre alphabétique{end_lig2}")
        print(f"32. Affichage des joueurs par score             {end_lig2}")
        print(f"33. Affichage de tous les tournois              {end_lig2}")
        print(f"34. Affichage des joueurs par ordre alphatours  {end_lig2}")
        print(f"35. Affichage des joueurs par score et par tours{end_lig2}")
        print(f"36. retour au menu principal                    {end_lig2}")
        print(f"--------------------------------------------------{end_lig1}")

    def choice_to_quit(self):
        confirm = input("Si vous souhaitez quitter, tapez 0 : ")
        return confirm

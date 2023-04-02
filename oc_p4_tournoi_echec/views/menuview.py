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
        print(f"---------------------Menu principal-----------------{ end_lig1}")
        print(f"----------------------------------------------------{ end_lig1}")
        print(f"----------------------------------------------------{ end_lig1}")
        print(f"1. Créer un tournoi                  ---------------{ end_lig1}")
        print(f"2. Sélectionner un tournoi           ---------------{ end_lig1}")
        print(f"3. Liste des tournois                ---------------{ end_lig1}")
        print(f"4. Quitter le programme              ---------------{ end_lig1}")
        print(f"----------------------------------------------------{ end_lig1}")

    def display_tournaments_submenu(self, tournament: Tournament):
        """affichage du menu du tournoi"""
        end_lig1 = "-----------------|"
        end_l2 = "                -------|"
        print("")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"----------------Sous-Menu du tournoi--------------{end_lig1}")
        print(f"--------------------------------------------------{end_lig1}")
        print(f"21. Ajouter un joueur                       {end_l2}")
        print(f"22. Générer les tours et les matchs         {end_l2}")
        print(f"23. Saisie des scores                       {end_l2}")
        print(f"24. Liste des joueurs par classement        {end_l2}")
        print(f"25. Liste des joueurs par ordre alphabétique{end_l2}")
        print(f"26. Liste des rounds et  matchs             {end_l2}")
        print(f"29. retour au menu supérieur                {end_l2}")
        print(f"--------------------------------------------------{end_lig1}")

    def choice_to_quit(self):
        confirm = input("Si vous souhaitez quitter, tapez 0 : ")
        return confirm

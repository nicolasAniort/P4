class RoundView():

    def __init__(self):
        pass

    def display_round1_create(self, tournament):
        print("Le round 1 est créé! Le tournoi peut débuter!")
        
    def display_file_exist(self, tournament):
        print("Le fichier existe déjà, le tournoi peut débuter!")    
            
    def display_active_round(self, name, path, data):
        # afficher le round et la liste de match
        print(f"Mise à jour du {name} ")
        print(f"Liste des match")
        for index, match in enumerate(data):
            player1 = match['match']['player1']['prenom'] + ' ' + match['match']['player1']['nom']
            player2 = match['match']['player2']['prenom'] + ' ' + match['match']['player2']['nom']
            print(f"Match {index+1}: joueur 1: {player1} - joueur 2: {player2}")
        
        # Demander à l'utilisateur l'ID du match à modifier
        match_id = input("Entrez l'ID du match à modifier : ")
        return match_id
        
    def update_score_player1(self):
        # Demander à l'utilisateur les scores pour le joueur1
                score1 = input("Entrez le score pour le joueur 1 : ")
                return score1
    def update_score_player2(self):
        # Demander à l'utilisateur les scores pour le joueur2
                score2 = input("Entrez le score pour le joueur 2 : ")
                return score2       
    def display_score_update_ok(self):
        print("Le score du match a été mis à jour avec succès.")
        
    
      
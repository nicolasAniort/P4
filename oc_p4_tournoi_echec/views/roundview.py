class RoundView():

    def __init__(self):
        pass

    def display_round1_create(self, tournament):
        print("Le round 1 est créé! Le tournoi peut débuter!")
    def display_round_create(self, tournament):
        print(f'Le round {tournament["numero_round_actif"]} est créé!')    
    def display_file_exist(self, tournament):
        print("Le fichier existe déjà, le tournoi peut débuter!")    
            
    def display_active_round(self, name, path, data):
        # afficher le round et la liste de match
        # trouver la taille maximale pour le nom et le prénom
        len_match = 5
        max_len_joueur = 15
        score = 5
        
        # Afficher l'en-tête de la table
        
        print("|--------------------------------------------------------------------|")
        print(f"|--------------------  MISE A JOUR DU {name}  -----------------------|")
        print("|--------------------     LISTE DES MATCHS     -----------------------|")
        print("|--------------------------------------------------------------------|")
        header = "| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |--------|".format("MATCH", len_match, "JOUEUR 1", max_len_joueur, "SCORE",score, "JOUEUR 2",max_len_joueur,"SCORE",score)
        separator = "|" + "-" * (len_match + (max_len_joueur * 2) + (score * 2) + 23) + "|"
        
        print(separator)
        print(header)
        print(separator)
        
        for index, match in enumerate(data):
            player1 = match['match']['player1']['prenom'] + ' ' + match['match']['player1']['nom']
            score1 = match['match']['score1']
            player2 = match['match']['player2']['prenom'] + ' ' + match['match']['player2']['nom']
            score2 = match['match']['score2']
            content = "| {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} |--------|".format(str(index+1), len_match,str(player1), max_len_joueur,str(score1),score,str(player2),max_len_joueur,str(score2),score)
            print(content)
            
        print(separator)
        print("")
        # Demander à l'utilisateur l'ID du match à modifier
        match_id = input("Entrez l'ID du match à modifier : ")
        return match_id
 
    def display_end_current_round(self,tournament):
        print(f'Le round {tournament.get("numero_round_actif")-1} est terminé!')
        print(f'Pensez à générer le round {tournament.get("numero_round_actif")}!')
        
    def update_score_player1(self):
        # Demander à l'utilisateur les scores pour le joueur1
                score1 = input("Entrez le score pour le joueur 1 : ")
                return score1
    
    def update_score_player2(self):
        # Demander à l'utilisateur les scores pour le joueur2
                score2 = input("Entrez le score pour le joueur 2 : ")
                return score2                   
       
    def display_id_match_unknow(self):
        print("Aucun match trouvé avec cet ID.")        
    def display_score_update_ok(self):
        print("Le score du match a été mis à jour avec succès.")
        
    
      
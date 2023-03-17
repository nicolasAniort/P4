from ast import List
import random
import json
from typing import Any, Dict
from models.tournament import Tournament
from models.match import Match
from views.roundview import RoundView   
import json
class MatchEncoder(json.JSONEncoder):
        "sert à la serialisation des matchs dans le fichier json"
        def default(self, o: Any) -> Dict[str, Any]:
            if isinstance(o, Match):
                return {
                    "player1": o.players[0],
                    "player2": o.players[1],
                    "score1": o.scores[0],
                    "score2": o.scores[1]
                }
            return super().default(o)  
class RoundController():
    
    def __init__(self):
            pass
    """ Creation des rounds"""    
    def create_round(self, tournament):
        count = int(tournament.get("numero_round_actif"))
        player_list_file = tournament.get("liste_des_joueurs")

        with open(player_list_file, "r") as file:
            file_contents = file.read()
            player_data = json.loads(file_contents)

        list_players = player_data

        self.name = "Round" + str(count)
        self.nbmatch = len(list_players) / 2
        round_list = []
        # Si on crée le premier round
        if count == 1:
            rank_match = 1
            random.shuffle(list_players)
            match_list = []
            for index_list_player, index_list_playertwo in zip(range(0, len(list_players), 2), range(1, len(list_players), 2)):
                match_player1 = list_players[index_list_player]
                match_player2 = list_players[index_list_playertwo]

                match = Match(match_player1, match_player2)

                new_round_match_file = {
                    "id_round": str(rank_match),
                    "match": match
                }
                match_list.append(new_round_match_file)
                rank_match = rank_match + 1
                
            round_list.append(match_list)
            file_path = 'data/rounds/' + tournament.get("id du tournoi") + self.name + '.json'
            try:
                with open(file_path, 'x') as file:
                    json.dump(match_list, file, cls=MatchEncoder, indent=2)
            except:
                RoundView.display_file_exist(self, tournament)
        else:
            # Récupération des résultats du round précédent
            previous_round_number = count - 1
            previous_round_file = 'data/rounds/' + tournament.get("id du tournoi") + 'Round' + str(previous_round_number) + '.json'
            with open(previous_round_file, 'r') as f:
                previous_round = json.load(f)

            # Tri des joueurs en ordre décroissant de score
            players_scores = {}
            for match in previous_round:
                result = match['match'].get_result()
                if result is not None:
                    players_scores[match['match'].get_player1()] = players_scores.get(match['match'].get_player1(), 0) + result[0]
                    players_scores[match['match'].get_player2()] = players_scores.get(match['match'].get_player2(), 0) + result[1]

            sorted_players = sorted(list_players, key=lambda player: players_scores.get(player['nom'] + ' ' + player['prenom'], 0), reverse=True)

            # Création des matches du nouveau round
            rank_match = 1
            match_list = []
            played_matches = []

            for index_list_player, index_list_playertwo in zip(range(0, len(sorted_players), 2), range(1, len(sorted_players), 2)):
                match_player1 = sorted_players[index_list_player]['nom'] + ' ' + sorted_players[index_list_player]['prenom']
                match_player2 = sorted_players[index_list_playertwo]['nom'] + ' ' + sorted_players[index_list_playertwo]['prenom']

                # Vérification que les joueurs n'ont pas déjà joué ensemble dans les rounds précédents
                already_played = False
                for match in previous_round:
                    if (match_player1 in [match['match'].get_player1(), match['match'].get_player2()] and
                        match_player2 in [match['match'].get_player1(), match['match'].get_player2()]):
                        already_played = True
                        break

                # Si les joueurs n'ont pas déjà joué ensemble, on crée un nouveau match
                if not already_played:
                    match = Match(match_player1, match_player2)
                    new_round_match_file = {
                        "id_round": str(rank_match),
                        "match": match
                    }
                    match_list.append(new_round_match_file)
                    rank_match += 1
                    played_matches.append((match_player1, match_player2))

            # Si tous les matches n'ont pas été créés, on crée des matches aléatoires pour les joueurs restants
            if len(match_list) < self.nbmatch:
                remaining_players = [player['nom'] + ' ' + player['prenom'] for player in sorted_players if player['nom'] + ' ' + player['prenom'] not in [match[0] for match in played_matches] + [match[1] for match in played_matches]]
                random.shuffle(remaining_players)
                for index in range(0, len(remaining_players), 2):
                    match_player1 = remaining_players[index]
                    match_player2 = remaining_players[index + 1]
                    match = Match(match_player1, match_player2)
                    new_round_match_file = {
                        "id_round": str(rank_match),
                        "match": match
                    }
                    match_list.append(new_round_match_file)
                    rank_match += 1

            round_list.append(match_list)

            # Enregistrement des matches du nouveau round dans un fichier JSON
            file_path = 'data/rounds/' + tournament.get("id du tournoi") + self.name + '.json'
            try:
                with open(file_path, 'x') as file:
                    json.dump(match_list, file, cls=MatchEncoder, indent=2)
            except:
                pass

            #return round_list       
        
        RoundView.display_round1_create(self, tournament)
        
    def update_round(self, tournament):
        count = int(tournament.get("numero_round_actif"))
        self.name = "Round" + str(count)
        file_path = 'data/rounds/' + tournament.get("id du tournoi") + self.name + '.json'
        
        with open(file_path, 'r') as file:
                file_contents = file.read()
                round_data = json.loads(file_contents)
                
        # afficher le round et la liste de match
        id_selected = RoundView.display_active_round(self, self.name, file_path, round_data)
        # Parcourir la liste round_data pour trouver le match correspondant
        
        for number,match in enumerate(round_data):
            
            if match['id_round'] == id_selected:
                
                # Demander à l'utilisateur les scores pour chaque joueur
                
                score1 = RoundView.update_score_player1(self)
                score2 = RoundView.update_score_player2(self)

                # Mettre à jour les scores correspondants dans le dictionnaire du match
                match['match']['score1'] = score1
                match['match']['score2'] = score2
                round_data[number] = match
                # Enregistrer les modifications dans le fichier
                with open(file_path, 'w') as file:
                    json.dump(round_data, file, cls=MatchEncoder, indent=2)

                print("Le score du match a été mis à jour avec succès.")
                #RoundController.check_round(self, tournament)
                break
            else:
                print("Aucun match trouvé avec cet ID.")
                #RoundController.check_round(self, tournament)
        
    def check_round(self, tournament):
        round_number = int(tournament.get("numero_round_actif"))
        tournament_id = tournament.get("id du tournoi")
        self.name = "Round" + str(round_number)
        file_path = 'data/rounds/' + tournament_id + self.name + '.json'
        
        with open(file_path, 'r') as file:
            file_contents = file.read()
            round_list = json.load(file_contents)
        
        # Vérification si tous les matchs ont été joués
        all_played = True
        for match_file in round_list:
            match = match_file['match']['score1']
            if match is None:
                all_played = False
                break

        # Clôture du round si tous les matchs ont été joués
        if all_played:
            tournament.tournament_round_number = round_number + 1
            
        
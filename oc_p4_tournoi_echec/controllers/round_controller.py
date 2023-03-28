import random
import json
from typing import Any, Dict
from controllers.tournament_controller import TournamentController
from models.match import Match
from views.roundview import RoundView


class MatchEncoder(json.JSONEncoder):
    "sert à la serialisation des matchs dans le fichier json"

    def default(self, o: Any) -> Dict[str, Any]:
        if isinstance(o, Match):
            return {
                "player1": o.players[0],
                "player2": o.players[1],
                "score1": o.scores[0],
                "score2": o.scores[1],
            }
        return super().default(o)


class RoundController:
    def __init__(self):
        pass

    """ Creation des rounds"""

    def create_round(self, tournament):
        count = int(tournament.get("numero_round_actif"))
        player_list_file = tournament.get("liste_des_joueurs")

        # lecture de la liste des joueurs du tournoi pour créer les matchs
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
            # creation aléatoire des match
            for index_list_player, index_list_playertwo in zip(
                range(0, len(list_players), 2), range(1, len(list_players), 2)
            ):
                match_player1 = list_players[index_list_player]
                match_player2 = list_players[index_list_playertwo]

                match = Match(match_player1, match_player2)
                # création du nouveau round
                new_round_file = {"id_round": str(rank_match), "match": match}
                match_list.append(new_round_file)
                rank_match = rank_match + 1

            round_list.append(match_list)
            file_path = (
                "data/rounds/"
                + tournament.get("id du tournoi")
                + self.name + ".json"
            )
            try:
                with open(file_path, "x") as file:
                    json.dump(match_list, file, cls=MatchEncoder, indent=2)
            except FileExistsError:
                RoundView.display_file_exist(self, tournament)
        else:
            # Récupération des résultats
            players_data_file = (
                "data/tournaments/"
                + tournament.get("id du tournoi")
                + "_players.json"
            )
            players_data = []
            with open(players_data_file, "r") as f:
                players_data = json.load(f)

            # Tri des joueurs en ordre décroissant de score
            sorted_players = sorted(
                players_data, key=lambda player: player["classement"]
            )

            # Création des matches du nouveau round
            rank_match = 1
            match_list = []
            played_matches = []

            # creation des matchs par joueurs consecutifs

            for index_list_player, index_list_playertwo in zip(
                range(0, len(sorted_players), 2
                      ), range(1, len(sorted_players), 2)
            ):
                player1 = sorted_players[index_list_player]
                id_player1 = player1["identifiant_national"]
                player2 = sorted_players[index_list_playertwo]
                adversary_player2 = player2["adversaire"]

                # Vérification que les joueurs n'ont pas déjà joué ensemble
                # dans les rounds précédents
                # doit etre verifié grace à la liste des adversaire deja
                # rencontré player ["adversaire"]
                already_played = False
                for number, adversary in enumerate(adversary_player2):
                    if id_player1 == adversary[number]:
                        already_played = True

                # Si les joueurs n'ont pas déjà joué ensemble,
                # on crée un nouveau match
                if not already_played:
                    match_player1 = sorted_players[index_list_player]
                    match_player2 = sorted_players[index_list_playertwo]

                    match = Match(match_player1, match_player2)

                    new_round_file = {"id_round": str(
                        rank_match), "match": match}
                    match_list.append(new_round_file)
                    rank_match += 1
                    played_matches.append((match_player1, match_player2))

            # Si tous les matches n'ont pas été créés, on crée des matches
            # aléatoires pour les joueurs restants
            if len(match_list) < self.nbmatch:
                remaining_players = [
                    player["nom"] + " " + player["prenom"]
                    for player in sorted_players
                    if player["nom"] + " " + player["prenom"]
                    not in [match[0] for match in played_matches]
                    + [match[1] for match in played_matches]
                ]
                random.shuffle(remaining_players)
                for index in range(0, len(remaining_players), 2):
                    match_player1 = remaining_players[index]
                    match_player2 = remaining_players[index + 1]
                    match = Match(match_player1, match_player2)
                    new_round_match_file = {"id_round": str(
                        rank_match), "match": match}
                    match_list.append(new_round_match_file)
                    rank_match += 1

            round_list.append(match_list)

            # Enregistrement des matches du nouveau round dans un fichier JSON
            file_path = (
                "data/rounds/"
                + tournament.get("id du tournoi")
                + self.name + ".json"
            )
            try:
                with open(file_path, "x") as file:
                    json.dump(match_list, file, cls=MatchEncoder, indent=2)
            except FileNotFoundError:
                pass

            # return round_list

        RoundView.display_round_create(self, tournament)

    """Mise à jour du round"""

    def update_round(self, tournament):
        # intialisation des chemin de fichiers
        count = int(tournament.get("numero_round_actif"))
        self.name = "Round" + str(count)
        file_path = (
            "data/rounds/"
            + tournament.get("id du tournoi")
            + self.name + ".json"
        )
        update_player_tournament_path = (
            "data/tournaments/"
            + tournament.get("id du tournoi")
            + "_players.json"
        )

        # lecture du fichier du round actif
        with open(file_path, "r") as file:
            file_contents = file.read()
            round_data = json.loads(file_contents)
        # lecture du fichier player_data.json
        with open(update_player_tournament_path, "r") as file:
            file_contents = file.read()
            players_data = json.loads(file_contents)

        # afficher le round et la liste de match
        id_selected = RoundView.display_active_round(
            self, self.name, file_path, round_data
        )

        # Parcourir la liste round_data pour trouver le match correspondant
        for number, match in enumerate(round_data):
            if match["id_round"] == id_selected and int(id_selected
                                                        ) <= len(round_data):
                # Demander à l'utilisateur les scores pour chaque joueur
                score1 = RoundView.update_score_player1(self)
                score2 = RoundView.update_score_player2(self)

                # Mettre à jour les scores
                # dans le dictio du match
                match["match"]["score1"] = score1
                match["match"]["score2"] = score2
                # round_data[number] = match

                # Mettre à jour les classement dans le dictio du match
                match["match"]["player1"]["classement"] = score1
                match["match"]["player1"]["adversaire"].append(
                    match["match"]["player2"]["identifiant_national"]
                )
                match["match"]["player2"]["classement"] = score2
                match["match"]["player2"]["adversaire"].append(
                    match["match"]["player1"]["identifiant_national"]
                )

                for player in players_data:
                    if (
                        player["identifiant_national"]
                        == match["match"]["player1"]["identifiant_national"]
                    ):
                        match_order = match["match"]["player1"]["classement"]
                        player["classement"] = match_order
                        player["adversaire"].append(
                            match["match"]["player2"]["identifiant_national"]
                        )

                    elif (
                        player["identifiant_national"]
                        == match["match"]["player2"]["identifiant_national"]
                    ):
                        match_order2 = match["match"]["player2"]["classement"]
                        player["classement"] = match_order2
                        player["adversaire"].append(
                            match["match"]["player1"]["identifiant_national"]
                        )

                # Enregistrer les modification
                # dans le fichier TRXXXXXXX_players.json
                with open(update_player_tournament_path, "w") as file:
                    json.dump(players_data, file, cls=MatchEncoder, indent=2)

                round_data[number] = match

                # Enregistrer les modifications dans le fichier du round
                with open(file_path, "w") as file:
                    json.dump(round_data, file, cls=MatchEncoder, indent=2)

                RoundView.display_score_update_ok(self)
                RoundController.check_round(self, tournament)
                TournamentController.tournament_rank_players_update(
                    self, tournament, match
                )
                break
            elif match["id_round"] != id_selected and int(id_selected) <= len(
                round_data
            ):
                pass
            elif int(id_selected) > len(round_data):
                RoundView.display_id_match_unknow(self)
                RoundController.check_round(self, tournament)

    """Verification de fin de round"""

    def check_round(self, tournament):
        round_number = int(tournament.get("numero_round_actif"))
        tournament_id = tournament.get("id du tournoi")
        self.name = "Round" + str(round_number)
        file_path = "data/rounds/" + tournament_id + self.name + ".json"

        with open(file_path, "r") as file:
            file_contents = file.read()
            round_list = json.loads(file_contents)

        # Vérification si tous les matchs du round ont été joués
        all_played = True
        for match_file in round_list:
            match = match_file["match"]["score1"]
            if match is None:
                all_played = False
                break

        # Clôture du round si tous les matchs ont été joués
        if all_played == True:
            # mise a jour numero du round actif
            tournament.update({"numero_round_actif": round_number + 1})
            # recuperation de lid du tournoi actif
            prefixed_tournament = tournament.get("id du tournoi")
            # chemin du fichier tournament_data.json
            tournamentfilepath = "data/tournaments/tournament_data.json"
            tournaments = []
            # recuperation du contenu du fichier
            # tournament_data dans tournament
            with open(tournamentfilepath, "r") as file:
                tournaments = json.load(file)

            for number, tournamentwrite in enumerate(tournaments):
                # recherche du tournoi actif dans la liste des tournois
                if tournamentwrite["id du tournoi"] == prefixed_tournament:
                    # additionner le score au score existant
                    tournamentwrite["numero_round_actif"] = tournament[
                        "numero_round_actif"
                    ]

                    # Enregistrer les modifications dans le fichier du tournoi
                    with open(tournamentfilepath, "w") as file:
                        json.dump(tournaments, file, indent=2)

            RoundController.create_round(self, tournament)
            RoundView.display_end_current_round(self, tournament)

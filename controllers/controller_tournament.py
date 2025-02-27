from views.json_manager import JSONManager
from models.model_tournament import Tournament
from views.menu import MenuView
from models.model_round import Round
from models.model_player import Player
import random


class TournamentController:
    def __init__(self):
        self.players_candidates = []
        self.tournaments = []
        self.load_tournaments_from_json("tournaments.json")
        self.load_players_from_candidates("players_candidates.json")
        self.MenuView = MenuView
        self.selected_tournament = None

    def save_tournaments_to_json(self, filename="tournaments.json"):
        data = {
            "tournaments": [
                {
                    "name": tournament.name,
                    "place": tournament.place,
                    "beginning_date": tournament.beginning_date.strftime("%d/%m/%Y"),
                    "end_date": tournament.end_date.strftime("%d/%m/%Y"),
                    "description": tournament.description,
                    "number_of_rounds": tournament.number_of_rounds,

                    "players": [
                        # Vérifier le type de player
                        player.to_dict()
                        for player in tournament.players
                    ],
                    "rounds": [round.to_dict() for round in tournament.rounds],  # Utilisation de to_dict
                }
                for tournament in self.tournaments
            ]
        }
        JSONManager.save_to_file(data, filename)

    def load_tournaments_from_json(self, filename: str = "tournaments.json"):
        # Charger les données JSON
        data = JSONManager.load_from_file(filename)
        if data and "tournaments" in data:
            self.tournaments = []
            for tournament_data in data["tournaments"]:
                tournament_data = Tournament.from_dict(data=tournament_data)
                self.tournaments.append(tournament_data)

    def add_new_tournament(self):
        # Récupération des données du tournoi depuis la vue
        tournament_data = MenuView.add_new_tournament()
        # Création et initialisation du nouveau tournoi
        new_tournament = Tournament(
            name=tournament_data["name"],
            place=tournament_data["place"],
            beginning_date=tournament_data["beginning_date"],
            end_date=tournament_data["end_date"],
            description=tournament_data["description"],
            players=[],  # Liste des joueurs vide par défaut
            selected_tournament=[],  # Aucun tournoi sélectionné par défaut
            rounds=[],  # Aucun round initial
            generate_pairs=[]  # Pas de paires générées initialement
        )

        # Ajout du tournoi à la liste des tournois
        self.tournaments.append(new_tournament)

        # Sauvegarde des tournois dans un fichier JSON
        self.save_tournaments_to_json()

        # Message de confirmation pour l'utilisateur
        self.MenuView.display_message(f"Le nouveau tournoi '{new_tournament.name}' a été ajouté avec succès.")

    def load_players_from_candidates(self, filename="players_candidates.json"):
        """
        Charge les joueurs depuis le fichier players_candidates.json.
        """
        data = JSONManager.load_from_file(filename)
        if data and "players_candidates" in data:
            self.players_candidates = []
            for player_data in data["players_candidates"]:
                self.players_candidates.append(Player.from_dict(player_data))
        else:
            MenuView.display_message("Aucun joueur candidat trouvé ou fichier incorrect.")

    def save_players_to_tournament_json(self):
        """
        Sauvegarde les joueurs sélectionnés dans le fichier tournaments.json.
        """
        if not self.selected_tournament:
            MenuView.display_message("Aucun tournoi sélectionné. Impossible de sauvegarder les joueurs.")
            return

        # Mettre à jour les joueurs du tournoi sélectionné dans la liste des tournois
        for tournament in self.tournaments:
            if tournament.name == self.selected_tournament.name:
                tournament.players = self.selected_tournament.players
                break

        # Sauvegarder tous les tournois dans tournaments.json
        self.save_tournaments_to_json()

    def display_tournaments(self):
        return MenuView.display_tournaments(self.tournaments)

    def choice_tournament(self, index):
        if 0 <= index < len(self.tournaments):
            self.selected_tournament = self.tournaments[index]
            return self.selected_tournament
        return None

    def selected_players(self):
        """
        Sélectionner les joueurs pour le tournoi actuel.
        """
        if not self.selected_tournament:
            MenuView.display_message("No tournament selected.You mast select a tournament from this list\n")
            self.select_a_tournament()  # Demander à l'utilisateur de sélectionner un tournoi
            return
        MenuView.display_message(f"add players to 'tournament': {self.selected_tournament.name}")
        MenuView.display_players_candidates(self.players_candidates)
        while len(self.selected_tournament.players) < 8:
            choice = MenuView.get_player_number(len(self.selected_tournament.players) + 1,
                                                len(self.players_candidates))
            if 0 <= choice < len(self.players_candidates):
                player = self.players_candidates.pop(choice)
                self.selected_tournament.players.append(player)
                self.save_players_to_tournament_json()
                MenuView.display_message(f"Player {player.firstName} {player.lastName} selected.")
            else:
                MenuView.display_message("Invalid number. Please try again.")

    @staticmethod
    def generate_pairs(players, round_number, previous_pairs=None):
        MenuView.generate_pairs(players)

        """
       Génère des paires de joueurs en fonction de leurs scores (ordre décroissant).
       Si plusieurs joueurs ont le même score, ils sont randomisés entre eux.
       :param players: Liste des joueurs.
       :param previous_pairs: Liste des paires précédentes pour éviter les répétitions (optionnel).
       :return: Liste des paires de joueurs.
       """
        if round_number == 0:
            # Mélanger et générer des paires
            random.shuffle(players)
            pairs = [(players[i], players[i + 1]) for i in range(0, len(players) - 1, 2)]
            return pairs
        # Trier les joueurs par score (du plus élevé au plus bas)
        players.sort(key=lambda player: player.score, reverse=True)
        # Générer les paires en associant les joueurs dans l'ordre trié
        pairs = []
        used_players = set()
        for i in range(0, len(players), 2):
            playerA = players[i]
            playerB = players[i + 1] if i + 1 < len(players) else None

            # Éviter les matchs répétés si previous_pairs est fourni
            if previous_pairs and playerB:
                for pair in previous_pairs:
                    if (playerA in pair and playerB in pair):
                        # Trouver un autre joueur pour playerB
                        for j in range(i + 2, len(players)):
                            if players[j] not in used_players and (playerA, players[j]) not in previous_pairs:
                                playerB = players[j]
                                break
            if playerB:
                pairs.append((playerA, playerB))
                used_players.add(playerA)
                used_players.add(playerB)
        return pairs

    def playing_rounds(self):
        """
        Joue quatre rounds du tournoi en générant des paires et en mettant à jour les scores.
        """
        if not self.selected_tournament:
            MenuView.display_message("No tournament selected.You mast select a tournament from this list\n")
            self.select_a_tournament()  # Demande to user to select a tournament
            return

        if len(self.selected_tournament.players) < 8:
            MenuView.display_message("Errror : Atournament need at least 8 players.")
            return
        MenuView.display_message(f"start play 4 rounds of: 'Tournament': {self.selected_tournament.name}")
        previous_pairs = []  # Pour stocker les paires précédentes
        for i in range(1, self.selected_tournament.number_of_rounds + 1):
            MenuView.display_message(f"\n=== Round {i} ===")
            # Créer une instance de Round
            round_instance = Round(number=f"{i}")
            # Générer des paires en fonction des scores et éviter les répétitions
            pairs = self.generate_pairs(self.selected_tournament.players, round_number=i, previous_pairs=None)
            previous_pairs.extend(pairs)  # Ajouter les paires actuelles à la liste des paires précédentes
            # Jouer les matchs du round
            MenuView.playing_rounds(pairs, round_instance, self.selected_tournament)
            self.save_tournaments_to_json()
            # Ajouter le round au tournoi (uniquement s'il n'est pas déjà présent)
            if round_instance not in self.selected_tournament.rounds:
                self.selected_tournament.rounds.append(round_instance)
            # Sauvegarder les données mises à jour dans tournaments.json
            self.save_tournaments_to_json()

    def ordered_candidates_players_list(self):
        players_sorts = sorted(self.players_candidates, key=lambda p: (p.lastName, p.firstName))
        MenuView.ordered_candidates_players_list(players_sorts)

    def selected_tournament_details(self):
        """
        Génère un rapport détaillé pour un tournoi spécifique sélectionné par l'utilisateur.
        """
        # Vérifier s'il y a des tournois disponibles
        if not self.tournaments:
            MenuView.display_message("No tournaments available.")
            return
        # Afficher la liste des tournois
        MenuView.display_tournaments(self.tournaments)
        # Demande to user to choice a tournament
        try:
            tournament_choice = int(input("Enter the number of the tournament you want to display players for: "))
            if tournament_choice < 1 or tournament_choice > len(self.tournaments):
                MenuView.display_message("Invalid choice, please try again.")
                return

            # Selection of tournament choice
            selected_tournament = self.tournaments[tournament_choice - 1]
            # Verified ifdes players are present in the tournament
            if selected_tournament.players:
                MenuView.display_message(
                    f"\n● List of players in Tournament: *** {selected_tournament.name} ***")
                for player in selected_tournament.players:
                    MenuView.display_message(
                        f"- {player.lastName} {player.firstName} (ID: {player.birth_date})")
            else:
                MenuView.display_message(f"The selected tournament '{selected_tournament.name}' has no players.")
        except ValueError:
            MenuView.display_message("Invalid input. Please enter a valid number.")

    def display_ranking_players(self):
        if not self.selected_tournament:
            MenuView.display_message("No tournament selected.You mast select a tournament from this list\n")
            self.select_a_tournament()
            return
        self.select_a_tournament()
        MenuView.display_message(f"Display ranking of players / 'tournament': {self.selected_tournament.name}")
        # Trier les joueurs par score décroissant
        sorted_players = sorted(
            self.selected_tournament.players,
            key=lambda player: player.score,  # Assurez-vous que player.score est utilisé ici
            reverse=True
        )
        # Update the selected tournament's players list with the sorted list
        self.selected_tournament.players = sorted_players
        # Afficher le classement
        MenuView.display_players_ranking(sorted_players)
        # Sauvegarder les données mises à jour dans tournaments.json
        self.save_tournaments_to_json()

    def details_all_tournaments_rounds_and_matchs(self):
        """
        Generates a detailed report of all tournaments, rounds, and matchs,
        and saves the updated details in the JSON file.
        """
        if not self.tournaments:
            MenuView.display_message("No tournaments played.")
            return
        if self.selected_tournament:
            MenuView.display_message("\n=== List of Tournaments ===")
            MenuView.disply_all_details_rounds_and_matchs(self.tournaments)
            # Sauvegarde des détails des tournois dans le fichier JSON
            self.save_tournaments_to_json()
        else:
            MenuView.afficher_menu_principal()

    def ordered_all_tournament_players_list(self):
        # Vérifier s'il y a des tournois disponibles
        if not self.tournaments:
            MenuView.display_message("No tournaments available.")
            return
        # Afficher la liste des tournois
        self.display_tournaments()
        # Demande to user to choice a tournament
        try:
            tournament_choice = int(input("Enter the number of the tournament you want to display players for: "))
            if tournament_choice < 1 or tournament_choice > len(self.tournaments):
                MenuView.display_message("Invalid choice, please try again.")
                return
            # Selection of tournament choice
            selected_tournament = self.tournaments[tournament_choice - 1]
            # Verified ifdes players are present in the tournament
            if selected_tournament.players:
                MenuView.display_message(
                    f"\n● List of players in alphabetical order for '{selected_tournament.name}' tournament:")
                # Trier les joueurs par nom de famille puis prénom
                players_sorted = sorted(selected_tournament.players, key=lambda p: (p.lastName, p.firstName))
                for player in players_sorted:
                    MenuView.display_message(
                        f"- {player.lastName} {player.firstName} (ID: {player.birth_date})")
            else:
                MenuView.display_message(f"The selected tournament '{selected_tournament.name}' has no players.")
        except ValueError:
            MenuView.display_message("Invalid input. Please enter a valid number.")

    def select_a_tournament(self):
        # Displaying the list of tournament by view.
        self.display_tournaments()
        # Demande to user to choosing a tournament
        index = MenuView.get_tournament_choice()
        # Verified if the choice is valid
        if 0 <= index < len(self.tournaments):
            self.selected_tournament = self.tournaments[index]  # Mettre à jour le tournoi sélectionné
            MenuView.display_message(f"Vous avez sélectionné le tournoi : {self.selected_tournament.name}")
        else:
            MenuView.display_message("Numéro invalide. Aucun tournoi sélectionné.")

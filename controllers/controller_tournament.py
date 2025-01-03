from json_manager import JSONManager
from models.model_tournament import Tournament
from views.menu import MenuView
from models.model_round import Round
from models.model_player import Player
import random
import json


class TournamentController:
    def __init__(self):
        self.players_candidates = None
        self.tournaments = []
        self.load_tournaments_from_json("tournaments.json")
        self.players = []
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
                    "players": [player for player in tournament.players],
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
                # Charger les données des joueurs
                players = []
                for player_data in tournament_data.get("players", []):
                    # Vérifier si player_data est bien un dictionnaire
                    if not isinstance(player_data, dict):
                        continue
                    try:
                        # Tenter de créer une instance Player
                        player = Player(**player_data)
                        players.append(player)
                    except TypeError as e:
                        print(f"Error creating Player instance: {e}. Data: {player_data}")
                    except KeyError as e:
                        print(f"Missing key in player data: {e}. Data: {player_data}")
                # Trier les joueurs par ordre décroissant de leur score
                players.sort(key=lambda player: player.score, reverse=True)
                rounds = []
                for round_data in tournament_data.get("rounds", []):
                    # Harmonisation du champ 'matchs' en 'matches'
                    if 'matchs' in round_data:
                        round_data['matchs'] = round_data.pop('matchs')
                    # Suppression du champ 'end' s'il existe
                    round_data.pop('end', None)
                    try:
                        rounds.append(Round(**round_data))
                    except TypeError as e:
                        print(f"Error loading round data: {e}")
                try:
                    new_tournament = Tournament(
                        name=tournament_data["name"],
                        place=tournament_data["place"],
                        beginning_date=tournament_data["beginning_date"],
                        end_date=tournament_data["end_date"],
                        description=tournament_data["description"],
                        players=players,
                        rounds=rounds
                    )
                    self.tournaments.append(new_tournament)
                except KeyError as e:
                    print(f"Missing tournament data key: {e}")
                except TypeError as e:
                    print(f"Error loading tournament data: {e}")

    def add_new_tournament(self):
        # Récupération des données du tournoi depuis la vue
        tournament_data = self.MenuView.add_new_tournament()
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
            self.players_candidates = data["players_candidates"]
            print(f"{len(self.players_candidates)} joueurs candidats ont été chargés avec succès.")
        else:
            print("Aucun joueur candidat trouvé ou fichier incorrect.")

    def save_players_to_tournament_json(self):
        """
        Sauvegarde les joueurs sélectionnés dans un fichier spécifique au tournoi.
        """
        if not self.selected_tournament:
            print("No tournament selected. Cannot save players.")
            return

        # Construire le nom du fichier en fonction du nom ou de l'ID du tournoi
        tournament_file = f"{self.selected_tournament.name.replace(' ', '_')}_players.json"

        if len(self.selected_tournament.players) > 0:
            JSONManager.save_to_file({"players": self.selected_tournament.players}, tournament_file)
            print(
                f"{len(self.selected_tournament.players)} joueurs "
                f"ont été sauvegardés dans le fichier {tournament_file}."
            )
        else:
            print("Aucun joueur sélectionné à sauvegarder.")

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
            MenuView.display_message("No tournament selected.")
            return

        MenuView.display_players_candidates(self.players_candidates)

        while len(self.selected_tournament.players) < 8:
            choice = MenuView.get_player_number(len(self.selected_tournament.players) + 1,
                                                len(self.players_candidates))
            if 0 <= choice < len(self.players_candidates):
                player = self.players_candidates.pop(choice)
                self.selected_tournament.players.append(player)
                MenuView.display_message(f"Player {player['firstName']} {player['lastName']} selected.")
            else:
                MenuView.display_message("Invalid number. Please try again.")

    @staticmethod
    def generate_pairs(players):
        """
        Génère des paires aléatoires à partir de la liste de joueurs fournie.
        """
        if len(players) < 2:
            print("Pas assez de joueurs pour générer des paires.")
            return []

        # Mélanger et générer des paires
        random.shuffle(players)
        pairs = [(players[i], players[i + 1]) for i in range(0, len(players) - 1, 2)]
        return pairs

    def playing_4_rounds(self):
        # Play 4 rounds of the tournament.
        if not self.selected_tournament:
            MenuView.display_message("Error : No tournament has selected.")
            return
        if len(self.selected_tournament.players) < 8:
            print("Error: A tournament requires at least 8 players.")
            return
        for i in range(1, 5):
            print(f"\n=== Round {i} ===")
            # Créez l'instance de Round avec tous les paramètres nécessaires
            round_instance = Round(i)
            pairs = self.generate_pairs(self.selected_tournament.players)

            MenuView.playing_4_rounds(pairs, round_instance, self.selected_tournament)

    def ordered_candidates_players_list(self):
        players_sorts = sorted(self.players_candidates, key=lambda p: (p['lastName'], p['firstName']))
        MenuView.ordered_candidates_players_list(players_sorts)

    def selected_tournament_details(self):
        """
        Génère un rapport détaillé pour un tournoi spécifique sélectionné par l'utilisateur.
        """
        # Afficher la liste des tournois avec leurs numéros
        MenuView.display_tournaments(self.tournaments)

        # Demander à l'utilisateur de choisir un tournoi par son numéro
        tournament_choice = MenuView.get_tournament_choice()

        # Vérifier si le numéro est valide
        if 0 <= tournament_choice < len(self.tournaments):
            tournament = self.tournaments[tournament_choice]
            # Afficher les détails du tournoi sélectionné
            MenuView.selected_tournament_details(tournament)
        else:
            # Afficher un message si le numéro est invalide
            MenuView.display_message("invalid number.\n")

    @staticmethod
    def save_ranking_to_json(tournament, filename):
        if not tournament:
            print("No tournament selected for saving ranking.")
            return
        try:
            ranking = []
            # Enregistrer le classement dans un fichier JSON
            with open(filename, "w", encoding="utf-8") as file:
                json.dump({"ranking": ranking}, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"An error occurred while saving the ranking: {e}")

    def display_and_save_players_ranking(self):
        """
        Affiche le classement des joueurs pour le tournoi sélectionné
        et sauvegarde le classement dans un fichier JSON.
        """
        if not self.selected_tournament:
            MenuView.display_message("No tournament selected. Please select a tournament first.")
            return

        if not self.selected_tournament.players:
            MenuView.display_message("No players are registered in the tournament.")
            return

        # Trier les joueurs par score décroissant
        sorted_players = sorted(
            self.selected_tournament.players,
            key=lambda player: player['score'],  # Assurez-vous que player.score est utilisé ici
            reverse=True
        )
        for player in sorted_players:
            print("the finals score are:", (player['score']))
        # Afficher le classement
        MenuView.display_players_ranking(sorted_players)
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
            return MenuView.afficher_menu_principal()

    def ordered_all_tournament_players_list(self):
        # Vérifier s'il y a des tournois disponibles
        if not self.tournaments:
            MenuView.display_message("No tournaments available.")
            return

        # Afficher la liste des tournois
        MenuView.display_message("\n● List of available tournaments:")
        for index, tournament in enumerate(self.tournaments, start=1):
            MenuView.display_message(
                f"{index}. {tournament.name} (Location: {tournament.place}, "
                f"Dates: {tournament.beginning_date} - {tournament.end_date})")
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
                players_sorted = sorted(selected_tournament.players, key=lambda p: (p['lastName'], p['firstName']))
                for player in players_sorted:
                    MenuView.display_message(
                        f"- {player['lastName']} {player['firstName']} (ID: {player['birth_date']})")
            else:
                MenuView.display_message(f"The selected tournament '{selected_tournament.name}' has no players.")
        except ValueError:
            MenuView.display_message("Invalid input. Please enter a valid number.")

    def selected_tournaments(self):
        # Displaying the list of tournament by view.
        self.display_tournaments()
        # Demande to user to choosing a tournament
        index = MenuView.get_tournament_choice()
        # Verified if the choice is valid
        selected_tournament = self.choice_tournament(index)
        if selected_tournament:
            MenuView.display_message(f"You have selected the tournament: {selected_tournament.name}")
        else:
            MenuView.display_message("Invalid number. No selection made.")

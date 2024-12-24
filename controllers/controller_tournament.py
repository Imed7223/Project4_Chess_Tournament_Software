from models.model_match import Match
from models.model_tournament import Tournament
from views.menu import MenuView
from models.model_round import Round
from models.model_player import Player
import random


class TournamentController:
    def __init__(self):
        self.MenuView = MenuView
        self.selected_tournament = None
        self.players_candidates = [
            {"firstName": "Dupont", "lastName": "Jean", "birth_date": "1990-01-15", "national_id": "AB12345",
             "score": 0},
            {"firstName": "Martin", "lastName": "Sophie", "birth_date": "1992-03-22", "national_id": "CD67890",
             "score": 0},
            {"firstName": "Petit", "lastName": "Alain", "birth_date": "1985-06-10", "national_id": "EF13579",
             "score": 0},
            {"firstName": "Moreau", "lastName": "Lucie", "birth_date": "1989-08-12", "national_id": "GH24680",
             "score": 0},
            {"firstName": "Girard", "lastName": "Paul", "birth_date": "1991-04-19", "national_id": "IJ13579",
             "score": 0},
            {"firstName": "Blanc", "lastName": "Julie", "birth_date": "1987-12-30", "national_id": "KL46802",
             "score": 0},
            {"firstName": "Roux", "lastName": "Marc", "birth_date": "1993-05-16", "national_id": "MN75346", "score": 0},
            {"firstName": "Fontaine", "lastName": "Claire", "birth_date": "1995-09-23", "national_id": "OP15926",
             "score": 0},
            {"firstName": "Noir", "lastName": "Lucas", "birth_date": "1990-11-08", "national_id": "QR86420",
             "score": 0},
            {"firstName": "Perrot", "lastName": "Alice", "birth_date": "1986-03-14", "national_id": "ST97531",
             "score": 0},
            {"firstName": "Lopez", "lastName": "Hugo", "birth_date": "1988-06-05", "national_id": "UV24680",
             "score": 0},
            {"firstName": "Durand", "lastName": "Elodie", "birth_date": "1990-07-22", "national_id": "WX75313",
             "score": 0},
            {"firstName": "Lemoine", "lastName": "Yann", "birth_date": "1994-01-18", "national_id": "YZ24680",
             "score": 0},
            {"firstName": "Marchand", "lastName": "Eva", "birth_date": "1992-10-09", "national_id": "AB75364",
             "score": 0},
            {"firstName": "Gauthier", "lastName": "Nathan", "birth_date": "1993-11-12", "national_id": "CD53148",
             "score": 0},
            {"firstName": "Perrin", "lastName": "Louise", "birth_date": "1989-02-06", "national_id": "EF15937",
             "score": 0},
            {"firstName": "Robin", "lastName": "Tom", "birth_date": "1995-08-29", "national_id": "GH86420", "score": 0},
            {"firstName": "Leclerc", "lastName": "Emma", "birth_date": "1990-12-25", "national_id": "IJ75313",
             "score": 0},
            {"firstName": "Bertrand", "lastName": "Léo", "birth_date": "1991-03-03", "national_id": "KL46802",
             "score": 0},
            {"firstName": "Renaud", "lastName": "Marie", "birth_date": "1992-06-18", "national_id": "MN97531",
             "score": 0},
            {"firstName": "Fischer", "lastName": "Maxime", "birth_date": "1988-09-14", "national_id": "OP86420",
             "score": 0},
            {"firstName": "Schmidt", "lastName": "Amélie", "birth_date": "1994-05-03", "national_id": "QR15926",
             "score": 0},
            {"firstName": "Meyer", "lastName": "Alex", "birth_date": "1991-07-17", "national_id": "ST53148",
             "score": 0},
            {"firstName": "Chevalier", "lastName": "Sarah", "birth_date": "1987-01-10", "national_id": "UV97531",
             "score": 0},
            {"firstName": "Roussel", "lastName": "Victor", "birth_date": "1995-02-25", "national_id": "WX15937",
             "score": 0},
            {"firstName": "Lambert", "lastName": "Chloé", "birth_date": "1986-04-21", "national_id": "YZ75364",
             "score": 0},
            {"firstName": "Garcia", "lastName": "Simon", "birth_date": "1989-11-30", "national_id": "AB97531",
             "score": 0},
            {"firstName": "Morel", "lastName": "Anaïs", "birth_date": "1993-01-08", "national_id": "CD15926",
             "score": 0},
            {"firstName": "Fournier", "lastName": "Théo", "birth_date": "1992-09-19", "national_id": "EF75313",
             "score": 0},
        ]

        self.tournaments = [
            Tournament(
                name="Tournoi National",
                place="Grenoble",
                beginning_date="23/11/2022",
                end_date="25/11/2022",
                description="good organisation",
                players=[],
                selected_tournament=[],
                rounds=[],
            ),
            Tournament(
                name="Tournoi de Paris",
                place="Paris",
                beginning_date="20/11/2023",
                end_date="25/11/2023",
                description="better competition",
                players=[],
                selected_tournament=[],
                rounds=[],
            ),
            Tournament(
                name="Tournoi de challenge",
                place="Lyon",
                beginning_date="20/11/2024",
                end_date="25/11/2024",
                description="very good motivation",
                players=[],
                selected_tournament=[],
                rounds=[],
            ),
        ]

    def create_new_tournament(self, name, place, beginning_date, end_date, description):
        # Creating a new Tournament instance
        new_tournament = Tournament(
            name=name,
            place=place,
            beginning_date=beginning_date,
            end_date=end_date,
            description="description",
            players=[],  # Initialize with an empty player list
            selected_tournament=[],
            rounds=[],
        )

        # Add the new tournament to the existing list
        self.tournaments.append(new_tournament)
        return new_tournament

    def add_new_tournament(self):
        """
        Gère le processus de création d'un nouveau tournoi via la vue.
        """
        # Récupération des données du tournoi depuis la vue
        tournament = MenuView.add_new_tournament()
        # Création du tournoi
        new_tournament = self.create_new_tournament(
            name=tournament["name"],
            place=tournament["place"],
            beginning_date=tournament["beginning_date"],
            end_date=tournament["end_date"],
            description=tournament["description"],
        )
        MenuView.display_message(f"the new tournament: {new_tournament.name} is added succefully")

    def display_tournaments(self):
        return MenuView.display_tournaments(self.tournaments)

    def choice_tournament(self, index):
        if 0 <= index < len(self.tournaments):
            self.selected_tournament = self.tournaments[index]
            return self.selected_tournament
        return None

    def selected_players(self):
        if not self.selected_tournament:
            MenuView.view_message("No tournament selected. Please select a tournament first.")
            return

        MenuView.display_players_candidates(self.players_candidates)

        while len(self.selected_tournament.players) < 8:
            choice = MenuView.get_player_number(len(self.selected_tournament.players) + 1, len(self.players_candidates))
            if 0 <= choice < len(self.players_candidates):
                player = self.players_candidates.pop(choice)
                self.selected_tournament.players.append(player)
                MenuView.view_message(f"Player {player['firstName']} {player['lastName']} selected.")
            else:
                MenuView.view_message("Invalid number. Please try again.")

        MenuView.display_selected_players(self.selected_tournament.players)

    def generate_pairs(self, players):
        """Generates random pairs."""
        random.shuffle(players)
        pairs = [(players[i], players[i + 1]) for i in range(0, len(players), 2)]
        return pairs

    def playing_4_rounds(self):
        #Play 4 rounds of the tournament.
        if not self.selected_tournament:
            MenuView.display_message("Erreur : Aucun tournoi sélectionné.")
            return
        if len(self.selected_tournament.players) < 8:
            print("Error: A tournament requires at least 8 players.")

        for i in range(1, 5):
            print(f"\n=== Round {i} ===")
            round_instance = Round(i)
            pairs = self.generate_pairs(self.selected_tournament.players)
            MenuView.playing_4_rounds(pairs, round_instance, self.selected_tournament)

            '''for playerA, playerB in pairs:
                """All those combinations are wrongs : \
                                          \n(score_playerA == 1 and score_playerB != 0) or \
                                            \n(score_playerB == 1 and score_playerA != 0) or \
                                            \n(score_playerA == 0 and score_playerB == 0) or \
                                            \n(score_playerA == 0.5 and score_playerB != 0.5)")"""
                print(f"Match between: {playerA} vs {playerB}")

                try:
                    score1 = float(
                        input(f"Score of PlayerA: {playerA['firstName']} {playerA['lastName']} |you must choose  ("
                              f"0, 0.5, or 1): "))
                    score2 = float(
                        input(f"Score of PlayerB: {playerB['firstName']} {playerB['lastName']} |you must choose  ("
                              f"0, 0.5, or 1): "))
                    if (score1 == 1 and score2 != 0) or \
                            (score1 == 0 and score2 != 1) or \
                            (score1 == 0 and score2 == 0) or \
                            (score1 == 0.5 and score2 != 0.5) or \
                            (score1 not in [0, 0.5, 1] or score2 not in [0, 0.5, 1]) or \
                            (0 > score1 > 1 or 0 > score2 > 1):
                        MenuView.view_message("Error: Invalid score combination. Please press choice 4 to repeat.")
                        while score1 and score2 is True:
                            continue
                        return

                        # Displaying final scores
                        print(f"Final Score -> Player A: {total_score_playerA}, Player B: {total_score_playerB}")

                    match = Match(playerA, playerB)
                    match.save_result(score1, score2)
                    round_instance.matchs.append(match)

                    if score1 > score2:
                        print(f"Winners : {playerA['firstName']} {playerA['lastName']}")
                    elif score2 > score1:
                        print(f"Winners : {playerB['firstName']} {playerB['lastName']}")
                    else:
                        print("Draw match")
                except ValueError:
                    MenuView.display_message("Veuillez entrer des scores valides.")
            round_instance.finished()
            self.selected_tournament.rounds.append(round_instance)
            MenuView.display_message(round_instance)'''

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

    def display_players_ranking(self):
        if not self.selected_tournament:
            MenuView.display_message("No players are registered in the tournament.")
            return
        if self.selected_tournament.players:

            # Sorting players by descending score
            sorted_players = sorted(self.selected_tournament.players, key=lambda player: player['score'], reverse=True)
            MenuView.display_players_ranking(sorted_players)

    def details_all_tournaments_rounds_and_matchs(self):
        """
        Generates a detailed report of all tournaments, rounds, and matches, allowing the user to choose a tournament.
        """
        if not self.tournaments:
            MenuView.display_message("No tournaments available.")
            return
        MenuView.display_message("\n=== List of Tournaments ===")
        if self.selected_tournament:
            MenuView.disply_all_details_rounds_and_matchs(self.tournaments)
            self.display_players_ranking()
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
                f"{index}. {tournament.name} (Location: {tournament.place}, Dates: {tournament.beginning_date} - {tournament.end_date})")

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
        # Demande to user to choosong a tournament
        index = MenuView.get_tournament_choice()
        # Verified if the choice is valid
        selected_tournament = self.choice_tournament(index)
        if selected_tournament:
            MenuView.display_message(f"You have selected the tournament: {selected_tournament.name}")
        else:
            MenuView.display_message("Invalid number. No selection made.")

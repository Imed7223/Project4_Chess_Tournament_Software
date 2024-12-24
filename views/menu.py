import random
from models.model_round import Round
from models.model_match import Match
from models.model_player import Player
from models.model_tournament import Tournament


class MenuView:
    @staticmethod
    def afficher_menu_principal():
        return (
            "\n=== Main Menu ===\n"
            "1. Add a new tournament \n"
            "2. Selected tournaments\n"
            "3. Selected players\n"
            "4. start plying 4 rounds \n"
            "5. list of all candidates players in alphabetical order \n"
            "6. Displaying available tournaments \n"
            "7. selected tournament details \n"
            "8. list of all tournament players in alphabetical order \n"
            "9.details of all rounds and matchs and ranking players in tournaments \n"
            "10. Exit"
        )

    @staticmethod
    def get_choice():
        return input("Enter your choice : ")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_tournaments(tournaments):
        print("\n=== List of tournaments ===")
        for i, tournament in enumerate(tournaments):
            print(f"\n******Tournament n°{i + 1}****** ")
            print(f"\nName : {tournament.name}")
            print(f"Place : {tournament.place}")
            print(f"Dates : {tournament.beginning_date} - {tournament.end_date}")

    @staticmethod
    def get_tournament_choice():
        while True:
            try:
                choice = int(input("\nEnter the tournament number to select : ")) - 1
                return choice
            except ValueError:
                print("Please enter a valid number.")

    @staticmethod
    def display_players_candidates(players_candidates):
        if not players_candidates:
            print("\nNo player candidates available.")
            return

        print("\n=== List of candidate players ===")
        for i, player in enumerate(players_candidates):
            print(f"{i + 1}. {player['lastName']} {player['firstName']}  (ID: {player['national_id']})")

    @staticmethod
    def get_player_number(current_choice, max_candidates):
        """
        Asks the user to select a player by number.
        :param current_choice: Number of the current choice (1 to 8).
        :param max_candidates: Maximum number of candidate players.
        :return: Index of the selected player.
        """
        while True:
            try:
                choice = int(input(f"Enter player number (choice {current_choice}/8) : ")) - 1
                if 0 <= choice < max_candidates:
                    return choice
                else:
                    print("Invalid number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    @staticmethod
    def view_message(message):
        """
        Affiche un message à l'utilisateur.
        :param message: Message à afficher.
        """
        print(message)

    @staticmethod
    def display_selected_players(players):
        """
        Displaying list of selected players.
        """
        print("\n=== List of selected players ===")
        for i, player in enumerate(players):
            print(f"{i + 1}. {player['firstName']} {player['lastName']} (ID: {player['national_id']})")

    @staticmethod
    def generate_pairs(players):
        """Génère des paires aléatoires."""
        random.shuffle(players)
        pairs = [(players[i], players[i + 1]) for i in range(0, len(players), 2)]
        return pairs

    @staticmethod
    def display_players_ranking(players):
        """
        Displays the list of players in descending order of their scores.
        """
        print("=== Ranking of players ===: \
                \nTournament result :")
        for player in players:
            print(f"- {player['firstName']} {player['lastName']} (Score : {player['score']})")

    @staticmethod
    def ordered_candidates_players_list(players_candidates):
        print("\n● list of all candidate players in alphabetical order :")
        for player in players_candidates:
            print(f"- {player['lastName']} {player['firstName']} (ID : {player['birth_date']})")

    ''''@staticmethod
    def details_all_tournaments_rounds_and_matchs(tournaments):  '''

    @staticmethod
    def add_new_tournament():
        print("\n=== Création d'un nouveau tournoi ===")
        name = input("Nom du tournoi : ").strip()
        place = input("Lieu du tournoi : ").strip()
        beginning_date = input("Date de début (format JJ/MM/AAAA) : ").strip()
        end_date = input("Date de fin (format JJ/MM/AAAA) : ").strip()
        description = input("Description : ").strip()
        # Retourner les données sous forme de dictionnaire
        return {
            "name": name,
            "place": place,
            "beginning_date": beginning_date,
            "end_date": end_date,
            "description": description,
        }

    @staticmethod
    def selected_tournament_details(tournament):
        #display a specific tournament details
        print(f"\nDétails du tournoi :")
        print(f"Nom : {tournament.name}")
        print(f"Lieu : {tournament.place}")
        print(f"Dates : {tournament.beginning_date.strftime('%d/%m/%Y')} - {tournament.end_date.strftime('%d/%m/%Y')}")

    @staticmethod
    def playing_4_rounds(pairs, round_instance, selected_tournament):
        #Play 4 rounds of the tournament.
        for playerA, playerB in pairs:
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
                    print("Error: Invalid score combination. Please press choice 5 to repeat.")
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
        selected_tournament.rounds.append(round_instance)
        print(round_instance)

    @staticmethod
    def disply_all_details_rounds_and_matchs(tournaments):
        for index, tournament in enumerate(tournaments, 1):
            print(f"{index}. {tournament.name} - {tournament.place}")

        try:
            # Demander à l'utilisateur de choisir un tournoi
            choice = int(input("\nEnter the number of the tournament to view details: "))
            if choice < 1 or choice > len(tournaments):
                print("Invalid choice. Please select a valid tournament number.")
                return
            selected_tournament = tournaments[choice - 1]

            # Affichage des détails du tournoi sélectionné
            print(f"\n=== Rapport du tournoi : {selected_tournament.name} ===")
            print(f"Lieu : {selected_tournament.place}")
            print(
                f"Dates : {selected_tournament.beginning_date} - {selected_tournament.end_date}"
            )

            if not selected_tournament.rounds:
                print("No rounds have been played yet for this tournament.")
                return exit()

            print("\n=== Round Details ===")

            # Affichage des rounds et matchs du tournoi sélectionné
            for round_instance in selected_tournament.rounds:
                print(f"\nRound {round_instance.number}")
                print(f"Beginning : {round_instance.begining}")
                print(f"End : {round_instance.end if round_instance.end else 'Not finished'}")
                print("\nMatchs :")
                for match in round_instance.matchs:
                    print(
                        f"- {match.playerA['firstName']} {match.playerA['lastName']} (Score : {match.score_playerA}) "
                        f"vs {match.playerB['firstName']} {match.playerB['lastName']} (Score : {match.score_playerB})"
                    )

        except ValueError:
            print("Invalid input. Please enter a number.")
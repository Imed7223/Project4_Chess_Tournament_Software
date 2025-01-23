import random
from models.model_match import Match
from datetime import datetime
from models.model_player import Player
from tabulate import tabulate


class MenuView:
    @staticmethod
    def afficher_menu_principal():
        return (
            "\n=== Main Menu ===\n"
            "1. Add new tournament \n"
            "2. Selecte tournament\n"
            "3. Add players to selected tournament\n"
            "4. Play rounds on selected tournament \n"
            "5. Display detail of selected tournament \n"
            "6. Detail of all rounds on selected tournament \n"
            "7. Ranking of players on selected tournament \n"
            "8. list of all candidates players in alphabetical order \n"
            "9. list of all tournament players in alphabetical order \n"
            "10. Display all tournaments \n"
            "11. Exit"
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
            print(f"{i + 1}. {player.lastName} {player.firstName}  (ID: {player.national_id})")

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
    def display_selected_players(players):
        """
        Displaying list of selected players.
        """
        if not players:
            print("Aucun joueur sélectionné.", flush=True)
            return

        print("\n=== Liste des joueurs sélectionnés ===")
        for i, player in enumerate(players, start=1):
            # Vérifier si le joueur est un dictionnaire ou une instance de Player
            if isinstance(player, dict):
                # Si c'est un dictionnaire, accéder aux clés
                print(f"{i}. {player['firstName']} {player['lastName']} (ID: {player['national_id']})")
            elif isinstance(player, Player):
                # Si c'est une instance de Player, utiliser la notation pointée
                print(f"{i}. {player.firstName} {player.lastName} (ID: {player.national_id})")
            else:
                print(f"{i}. Type de joueur non reconnu : {type(player)}")

    @staticmethod
    def generate_pairs(players, previous_pairs=None):
        """
        Génère des paires de joueurs en fonction de leurs scores et évite les matchs répétés.
        :param players: Liste des joueurs.
        :param previous_pairs: Liste des paires précédentes pour éviter les répétitions.
        :return: Liste des paires de joueurs.
        """
        if len(players) < 2:
            print("Pas assez de joueurs pour générer des paires.")
            return []

        # Trier les joueurs par score (du plus élevé au plus bas)
        players.sort(key=lambda player: player.score, reverse=True)

        # Randomiser les joueurs ayant le même score
        i = 0
        while i < len(players) - 1:
            j = i
            while j < len(players) - 1 and players[j].score == players[j + 1].score:
                j += 1
            if j > i:
                random.shuffle(players[i:j + 1])
            i = j + 1

        pairs = []
        used_players = set()

        for i in range(0, len(players), 2):
            playerA = players[i]
            playerB = players[i + 1] if i + 1 < len(players) else None

            if previous_pairs and playerB:
                # Éviter les matchs répétés
                for pair in previous_pairs:
                    if (playerA in pair and playerB in pair):
                        for j in range(i + 2, len(players)):
                            if players[j] not in used_players and (playerA, players[j]) not in previous_pairs:
                                playerB = players[j]
                                break
            if playerB:
                pairs.append((playerA, playerB))
                used_players.add(playerA)
                used_players.add(playerB)
        return pairs

    @staticmethod
    def display_players_ranking(players):
        """
        Displays the list of players in descending order of their scores.
        """
        if not players:
            print("No players to display.", flush=True)
            return
        print("=== Ranking of players ===: \
                \nTournament result :")
        for player in players:
            # Utiliser la notation pointée pour accéder aux attributs de l'objet Player
            print(f"{player.firstName} {player.lastName} (Score : {player.score})", flush=True)

    @staticmethod
    def ordered_candidates_players_list(players_candidates):
        print("\n● list of all candidate players in alphabetical order :")
        for player in players_candidates:
            print(f"- {player.lastName} {player.firstName} (ID : {player.birth_date})")

    @staticmethod
    def add_new_tournament():
        print("\n=== Création d'un nouveau tournoi ===")

        while True:

            name = input("Nom du tournoi : ").strip()
            if name.replace(" ", "").isalpha():
                break
            print("Erreur : Le nom du tournoi doit contenir uniquement des lettres.")

        while True:
            place = input("Lieu du tournoi : ").strip()
            if place.replace(" ", "").isalpha():
                break
            print("Erreur : Le lieu doit contenir uniquement des lettres.")

        while True:
            beginning_date = input("Date de début (format JJ/MM/AAAA) : ").strip()
            try:
                beginning_date_obj = datetime.strptime(beginning_date, '%d/%m/%Y')
                break
            except ValueError:
                print("Erreur : Veuillez entrer une date valide au format JJ/MM/AAAA.")

        while True:
            end_date = input("Date de fin (format JJ/MM/AAAA) : ").strip()
            try:
                end_date_obj = datetime.strptime(end_date, '%d/%m/%Y')
                if end_date_obj >= beginning_date_obj:
                    break
                else:
                    print("Erreur : La date de fin doit être après la date de début.")
            except ValueError:
                print("Erreur : Veuillez entrer une date valide au format JJ/MM/AAAA.")

        while True:
            description = input("Description : ").strip()
            if description.replace(" ", "").isalpha():
                break
            print("Erreur : La description doit contenir uniquement des lettres.")

        # Retourner les données sous forme de dictionnaire
        return {
            "name": name,
            "place": place,
            "beginning_date": beginning_date_obj,
            "end_date": end_date_obj,
            "description": description,
        }

    @staticmethod
    def selected_tournament_details(tournament):
        # Display a specific tournament details
        print("\nDétails du tournoi :")
        print(f"Nom : {tournament.name}")
        print(f"Lieu : {tournament.place}")
        print(f"Dates : {tournament.beginning_date.strftime('%d/%m/%Y')} - {tournament.end_date.strftime('%d/%m/%Y')}")

    @staticmethod
    def playing_rounds(pairs, round_instance, selected_tournament):
        score1 = score2 = None
        # Play the rounds of the tournament.
        print(f"\n=== Pairs of players for {round_instance}===")
        """
           Affiche les paires de joueurs dans un tableau.
           :param pairs: Liste des paires de joueurs.
           """
        # Préparer les données pour le tableau
        table_data = []
        for i, (playerA, playerB) in enumerate(pairs, start=1):
            table_data.append([f"Pairs {i}", f"{playerA.firstName} {playerA.lastName} {playerA.score}", "vs",
                               f"{playerB.firstName} {playerB.lastName} {playerB.score}"])
        # Afficher le tableau
        print(tabulate(table_data, headers=["Pairs", "PlayerA", "vs", "PlayerB"], tablefmt="pretty"))
        print()
        for playerA, playerB in pairs:
            '''All those combinations are wrongs : \
                                          \n(score_playerA == 1 and score_playerB != 0) or \
                                            \n(score_playerB == 1 and score_playerA != 0) or \
                                            \n(score_playerA == 0 and score_playerB == 0) or \
                                            \n(score_playerA == 0.5 and score_playerB != 0.5)")'''
            print(f"{round_instance}")
            print(" *** Give a score and the winner of the Match *** ")
            print()
            valid_scores = False
            while not valid_scores:
                try:
                    score1_input = input(
                        f"Score of PlayerA: "
                        f"{playerA.firstName} {playerA.lastName} |you must choose ("
                        f"0, 0.5, or 1): ").strip()
                    score2_input = input(
                        f"Score of PlayerB: "
                        f"{playerB.firstName} {playerB.lastName} |you must choose ("
                        f"0, 0.5, or 1): ").strip()
                    # Check if the inputs are empty
                    if not score1_input or not score2_input:
                        print("Error: Empty score is invalid. Please try again.")
                        continue
                    # Convert inputs to float
                    score1 = float(score1_input)
                    score2 = float(score2_input)
                    # Validate scores
                    if score1 + score2 != 1:
                        print("Error: Invalid score combination. Please try again.")
                        continue
                    valid_scores = True  # Exit loop if inputs are valid
                except ValueError:
                    print("Error: Invalid input. Please enter a numeric score (0, 0.5, or 1).")
            # If valid scores are entered, proceed
            match = Match(playerA, playerB)
            match.save_result(score1, score2)
            round_instance.matchs.append(match)
            # Mettre à jour les scores des joueurs
            playerA.score += score1
            playerB.score += score2
            if score1 > score2:
                print(f" *** Winners *** : {playerA.firstName} {playerA.lastName}")
            elif score2 > score1:
                print(f" *** Winners *** : {playerB.firstName} {playerB.lastName}")
            else:
                print("Draw match")
        round_instance.finished()
        selected_tournament.rounds.append(round_instance)

    @staticmethod
    def disply_all_details_rounds_and_matchs(tournaments, sorted_players=None):
        for index, tournament in enumerate(tournaments, 1):
            print(f"{index}. {tournament.name} - {tournament.place}")
        try:
            # Demander à l'utilisateur de choisir un tournoi
            choice = int(
                input(
                    "\nEnter the number of the tournament to view details: "
                )
            )
            if choice < 1 or choice > len(tournaments):
                print("Invalid choice. "
                      "Please select a valid tournament number.")
                return
            selected_tournament = tournaments[choice - 1]
            # Affichage des détails du tournoi sélectionné
            print(f"\n=== Rapport du tournoi : {selected_tournament.name} ===")
            print(f"Lieu : {selected_tournament.place}")
            print(
                f"Dates : {selected_tournament.beginning_date} -"
                f" {selected_tournament.end_date}"
            )
            if not selected_tournament.rounds:
                print("No rounds have been played yet for this tournament.")
                return
            # Affichage des rounds et matchs du tournoi sélectionné
            for round_instance in selected_tournament.rounds:
                print("\n=== Round Details ===")
                print(f"\nRound {round_instance.number}")
                print(f"Beginning : {round_instance.beginning}")
                print(f"End : {round_instance.end}")
                print("\nMatchs :")
                for match in round_instance.matchs:
                    print(
                        f"- {match.playerA.firstName} {match.playerA.lastName} "
                        f"(Score: {match.score_playerA}) vs "
                        f"- {match.playerB.firstName} {match.playerB.lastName} "
                        f"(Score: {match.score_playerB})"
                    )
        except ValueError:
            print("Invalid input. Please enter a number.")

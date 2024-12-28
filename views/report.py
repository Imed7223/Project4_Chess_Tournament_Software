"""from views import menu
from views.menu import MenuView
from models.model_player import Player
from models.model_tournament import Tournament
from models.model_round import Round


class Report:
    def __init__(self):

    @staticmethod
    def afficher_rapport(self):
        print("\n" + "=" * 30)
        print("      Centre Échecs")
        print("         RAPPORTS")
        print("=" * 30)

        #self.liste_joueurs_ordonnees()
        #self.liste_tournois()
        #self.details_tournoi()
        self.afficher_rapport()
        self.details_rounds_and_matchs()
        self.display_players_ranking()

    def liste_joueurs_ordonnees(self):
        print("\n● Liste de tous les joueurs (ordre alphabétique) :")
        joueurs_tries = sorted(self.joueurs, key=lambda j: (j['nom'], j['prenom']))
        for joueur in joueurs_tries:
            print(f"- {joueur['nom']} {joueur['prenom']} (ID : {joueur['id_national']})")

    def liste_tournois(self):
        print("\n● Liste de tous les tournois :")
        for tournoi in self.controller.tournois:
            print(f"-Nom : {tournoi.nom} | Lieu : {tournoi.lieu} | Dates : {tournoi.date_debut} - {tournoi.date_fin}")

    def details_tournoi(self):
        tournoi = self.controller.tournois[0]  # Exemple : sélection du premier tournoi
        print(f"\n● Détails du tournoi '{tournoi.nom}' :")
        print(f"  Lieu : {tournoi.lieu}")
        print(f"  Dates : {tournoi.date_debut} - {tournoi.date_fin}")



    def details_rounds_and_matchs(self):
        
        #Generates a detailed report of tournament rounds and matches.
        
        if not self.controller.rounds:
            print("No rounds have been played yet.")
            return
        for tournament in self.controller.selected_tournament:
            print(f"\nRapport du tournoi : {tournament.name}")
            print(f"Lieu : {tournament.place}")
            print(
                f"Dates : {tournament.beginning_date.strftime('%d/%m/%Y')} - {tournament.end_date.strftime('%d/%m/%Y')}")
            print("\n=== Round Details ===")

        for round_instance in self.controller.rounds:
            print(f"\nRound {round_instance.number}")
            print(f"Beginning : {round_instance.begining}")
            print(f"End : {round_instance.end if round_instance.end else 'Not finished'}")
            print("\nMatchs :")
            for match in round_instance.matchs:
                print(
                    f"- {match.playerA['firstName']} {match.playerA['lastName']} (Score : {match.score_playerA}) "
                    f"vs {match.playerB['firstName']} {match.playerB['lastName']} (Score : {match.score_playerB})"
                )

    def display_players_ranking(self):
        
        #Displays the list of players in descending order of their scores.
        
        if not self.controller.players:
            print("No players are registered in the tournament.")
            return

        # Sorting players by descending score
        sorted_players = sorted(self.controller.players, key=lambda player: player['score'], reverse=True)
        print("\n=== Ranking of players ===")
        print("Tournament result :")
        for player in sorted_players:
            print(f"- {player['firstName']} {player['lastName']} (Score : {player['score']})")"""

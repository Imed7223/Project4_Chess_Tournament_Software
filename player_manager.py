from json_manager import JSONManager


class PlayerManager:
    def __init__(self):
        self.players = []

    def load_players_from_candidates(self, filename="players_candidates.json"):
        """
        Charge les joueurs depuis le fichier players_candidates.json.
        """
        data = JSONManager.load_from_file(filename)
        if data and "players_candidates" in data:
            self.players = data["players_candidates"]
            print(f"{len(self.players)} joueurs candidats ont été chargés avec succès.")
        else:
            print("Aucun joueur candidat trouvé ou fichier incorrect.")

    def save_players_to_json(self, filename="players.json"):
        """
        Sauvegarde les joueurs dans le fichier players.json.
        """
        if self.players:
            JSONManager.save_to_file({"players": self.players}, filename)
            print(f"{len(self.players)} joueurs ont été sauvegardés dans le fichier {filename}.")
        else:
            print("Aucun joueur à sauvegarder.")

from models.model_player import Player

class Match:
    def __init__(self, playerA, playerB, score_playerA=0.0, score_playerB=0.0):
        self.playerA = playerA
        self.playerB = playerB
        self.score_playerA = score_playerA
        self.score_playerB = score_playerB
        self.result = None  # Attribut pour stocker le résultat du match

    def __repr__(self):
        return (
            f"Match: {self.playerA.firstName} {self.playerA.lastName}"
            f" ({self.score_playerA} points)"
            f" vs {self.playerB.firstName} {self.playerB.lastName} "
            f"({self.score_playerB} points)"
        )

    def save_result(self, score_playerA, score_playerB):
        """Enregistre les scores et détermine le résultat du match."""
        self.score_playerA = score_playerA
        self.score_playerB = score_playerB

        if score_playerA > score_playerB:
            self.result = f"Winner: {self.playerA.firstName} {self.playerA.lastName}"
        elif score_playerB > score_playerA:
            self.result = f"Winner: {self.playerB.firstName} {self.playerB.lastName}"
        else:
            self.result = "Draw"

    def to_dict(self):
        """Convertit l'objet Match en dictionnaire."""
        return {
            "playerA": self.playerA.to_dict(),
            "playerB": self.playerB.to_dict(),
            "score_playerA": self.score_playerA,
            "score_playerB": self.score_playerB,
            "result": self.result,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Recrée un objet Match à partir d'un dictionnaire."""
        match = cls(
            playerA=Player.from_dict(data["playerA"]),
            playerB=Player.from_dict(data["playerB"]),
            score_playerA=data.get("score_playerA", 0.0),
            score_playerB=data.get("score_playerB", 0.0),
        )
        match.result = data.get("result", None)  # Charge le résultat s'il existe
        return match

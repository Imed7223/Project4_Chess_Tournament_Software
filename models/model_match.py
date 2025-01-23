from models.model_player import Player


class Match:
    def __init__(self, playerA, playerB, score_playerA=0.0, score_playerB=0.0):
        self.playerA = playerA
        self.playerB = playerB
        self.score_playerA = score_playerA
        self.score_playerB = score_playerB
        self.score = 0

    def __repr__(self):
        return (
            f"Match: {self.playerA.firstName} {self.playerA.lastName}"
            f" ({self.score_playerA} points)({self.score}points)"
            f"vs {self.playerB.firstName} {self.playerB.lastName} "
            f"({self.score_playerB} points)({self.score}points)"
        )

    def save_result(self, score_playerA, score_playerB):
        self.score_playerA = score_playerA
        self.score_playerB = score_playerB

    def to_dict(self):
        return {
            "playerA": self.playerA.to_dict(),
            "playerB": self.playerB.to_dict(),
            "score_playerA": self.score_playerA,
            "score_playerB": self.score_playerB,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            playerA=Player.from_dict(data["playerA"]),
            playerB=Player.from_dict(data["playerB"]),
            score_playerA=data["score_playerA"],
            score_playerB=data["score_playerB"],
        )

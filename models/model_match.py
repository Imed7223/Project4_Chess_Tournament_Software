class Match:
    def __init__(self, playerA, playerB, score_playerA=0.0, score_playerB=0.0):
        self.playerA = playerA
        self.playerB = playerB
        self.score_playerA = score_playerA
        self.score_playerB = score_playerB
        self.score = 0

    def __repr__(self):
        return (
            f"Match: {self.playerA.firstName} {self.playerA.lastName} ({self.score_playerA} points)({self.score}points)"
            f"vs {self.playerB.firstName} {self.playerB.lastName} ({self.score_playerB} points)({self.score}points)"
        )

    def save_result(self, score_playerA, score_playerB):
        # Mise à jour des scores du match.
        self.score_playerA = score_playerA
        self.score_playerB = score_playerB
        # Mise à jour des scores des joueurs
        self.playerA['score'] += score_playerA
        self.playerB['score'] += score_playerB

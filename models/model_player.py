import re


class Player:
    def __init__(self, firstName, lastName, birth_date, national_id, score=0):
        self.playerA = None
        self.score_playerB = None
        self.playerB = None
        self.score_playerA = None
        if not re.fullmatch(r"[A-Z]{2}\d{5}", national_id):
            raise ValueError("L'ID doit être au format 'AB12345'.")
        self.lastName = lastName
        self.firstName = firstName
        self.birth_date = birth_date
        self.national_id = national_id
        self.score = score

    def __repr__(self):
        return f"{self.firstName} {self.lastName} (ID: {self.national_id}, Score: {self.score})"

    def to_dict(self):
        return {
            "lastName": self.lastName,
            "firstName": self.firstName,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            firstName=data["firstName"],
            lastName=data["lastName"],
            birth_date=data["birth_date"],
            national_id=data["national_id"],
            score=data.get("score", 0)
        )

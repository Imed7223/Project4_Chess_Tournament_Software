import re

class Player:
    def __init__(self, firstName, lastName, birth_date, national_id, score=0):
        if not re.fullmatch(r"[A-Z]{2}\d{5}", national_id):
            raise ValueError("L'ID doit être au format 'AB12345'.")
        self.lastName = lastName
        self.firstName = firstName
        self.birth_date = birth_date
        self.national_id = national_id
        self.score = score

    def __repr__(self):
        return f"{self.firstName} {self.lastName} (ID: {self.national_id}, Score: {self.score})"

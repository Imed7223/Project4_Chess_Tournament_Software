from datetime import datetime


class Round:
    def __init__(self, number):
        self.number = number
        self.matchs = []
        self.begining = datetime.now()
        self.end = None

    def finished(self):
        self.end = datetime.now()


    def __repr__(self):
        return f"{self.number} - Begining: {self.begining}, End: {self.end}, Matchs: {len(self.matchs)}"



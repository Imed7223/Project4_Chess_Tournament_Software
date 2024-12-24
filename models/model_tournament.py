from datetime import datetime


class Tournament:
    def __init__(self, name, place, beginning_date, end_date, description,  players, selected_tournament, rounds):
        self.name = name
        self.place = place
        self.beginning_date = datetime.strptime(beginning_date, "%d/%m/%Y")
        self.end_date = datetime.strptime(end_date, "%d/%m/%Y")
        self.description = description
        self.players = []
        self.rounds = []
        self.selected_tournament = []
        self.generate_pairs = []
        self.selected_players = []
        self.rounds = []
    def __repr__(self):
        return f"{self.name} {self.place} (ID: {self.beginning_date}, Score: {self.end_date}, Description:{self.description})"



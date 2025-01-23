from datetime import datetime
from models.model_player import Player
from models.model_round import Round


class Tournament:
    def __init__(self, name, place, beginning_date, end_date, description, number_of_rounds=4,
                 generate_pairs=None, players=None, selected_tournament=None, rounds=None):
        self.name = name
        self.place = place
        # Gestion des différents formats pour beginning_date
        self.beginning_date = self.parse_date(beginning_date)
        # Gestion des différents formats pour end_date
        self.end_date = self.parse_date(end_date)
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.players = players or []
        self.rounds = rounds or []
        self.selected_tournament = selected_tournament or []
        self.generate_pairs = generate_pairs or []
        self.selected_players = []

    def parse_date(self, date_string):
        if isinstance(date_string, datetime):
            return date_string
        formats = [
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
            "%d/%m/%Y"
        ]
        for date_format in formats:
            try:
                return datetime.strptime(date_string, date_format)
            except ValueError:
                continue
        raise ValueError(f"Invalid date format: {date_string}")

    def __repr__(self):
        return (f"{self.name} {self.place} "
                f"(ID: {self.beginning_date}, Score: {self.end_date},"
                f" Description:{self.description})")

    def to_dict(self):
        return {
            "name": self.name,
            "place": self.place,
            "beginning_date": self.beginning_date.strftime('%Y-%m-%d %H:%M:%S'),
            "end_date": self.end_date.strftime('%Y-%m-%d %H:%M:%S'),
            "description": self.description,
            "players": [player.to_dict() for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
        }

    @classmethod
    def from_dict(cls, data):
        players = [Player.from_dict(p) for p in data.get("players", [])]
        rounds = [Round.from_dict(r) for r in data.get("rounds", [])]
        return cls(
            name=data["name"],
            place=data["place"],
            beginning_date=data["beginning_date"],
            end_date=data.get("end_date"),  # Utiliser .get() pour éviter les KeyError
            description=data["description"],
            players=players,
            rounds=rounds
        )

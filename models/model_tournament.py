from datetime import datetime


class Tournament:
    def __init__(self, name, place, beginning_date, end_date, description,
                 generate_pairs=None, players=None, selected_tournament=None, rounds=None):
        self.name = name
        self.place = place
        # Gestion des différents formats pour beginning_date
        self.beginning_date = self.parse_date(beginning_date)

        # Gestion des différents formats pour end_date
        self.end_date = self.parse_date(end_date)

        self.description = description
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
            "players": [player.national_id.to_dict() for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
        }

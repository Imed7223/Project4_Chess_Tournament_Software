from datetime import datetime
from models.model_match import Match


class Round:
    def __init__(self, number: int, matchs=None, beginning=None):
        self.number = number
        self.beginning = datetime.now() if not beginning else beginning
        self.end = datetime.now()
        self.matchs = matchs if matchs else []

    def finished(self):
        self.end = datetime.now()

    def __repr__(self):
        beginning_str = (
            self.beginning.strftime("%Y-%m-%d %H:%M:%S")
            if self.beginning
            else "Not started"
        )
        end_str = (
            self.end.strftime("%Y-%m-%d %H:%M:%S")
            if self.end
            else "Not finished"
        )
        return f"Round {self.number} - Beginning: {beginning_str}, End: {end_str}, Matchs: {len(self.matchs)}"

    def to_dict(self):
        return {
            "number": self.number,
            "matchs": [match.to_dict() if hasattr(match, 'to_dict') else match for match in self.matchs],
            "beginning": self.beginning
            if self.beginning
            else None,
            "end": self.end,
        }

    @classmethod
    def from_dict(cls, data):
        matchs = [Match.from_dict(match) if isinstance(match, dict) else match for match in data.get("matchs", [])]
        beginning = datetime.strptime(data["beginning"], "%Y-%m-%d %H:%M:%S") if data.get("beginning") else None
        end = datetime.strptime(data["end"], "%Y-%m-%d %H:%M:%S") if data.get("end") else None
        instance = cls(
            number=data["number"],
            matchs=matchs,
            beginning=beginning
        )
        if end:
            instance.end = end
        return instance

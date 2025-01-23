from datetime import datetime
from models.model_match import Match


class Round:
    def __init__(self, number: int, matchs=None, beginning=None):
        self.number = number
        self.beginning = datetime.now() if beginning is None else beginning
        self.end = None
        self.matchs = matchs if matchs else []

    def finished(self):
        self.end = datetime.now()

    def __repr__(self):
        beginning_str = (
            self.beginning.strftime("%Y-%m-%d %H:%M:%S")
            if self.beginning
            else "Not started"
        )
        return f"Round {self.number} - Beginning: {beginning_str}"

    def to_dict(self):
        return {
            "number": self.number,
            "matchs": [
                match.to_dict() if hasattr(match, "to_dict") else match
                for match in self.matchs
            ],
            "beginning": (
                self.beginning.strftime("%Y-%m-%d %H:%M:%S")
                if isinstance(self.beginning, datetime)
                else self.beginning
            ),
            "end": (
                self.end.strftime("%Y-%m-%d %H:%M:%S")
                if isinstance(self.end, datetime)
                else None
            ),
        }

    @classmethod
    def from_dict(cls, data):
        matchs = [Match.from_dict(m) for m in data.get("matchs", [])]
        beginning = (
            datetime.strptime(data["beginning"], "%Y-%m-%d %H:%M:%S")
            if data.get("beginning")
            else None
        )
        end = (
            datetime.strptime(data["end"], "%Y-%m-%d %H:%M:%S")
            if data.get("end")
            else None
        )
        obj = cls(number=data["number"], matchs=matchs, beginning=beginning)
        obj.end = end
        return obj

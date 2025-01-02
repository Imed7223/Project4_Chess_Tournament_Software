from datetime import datetime


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

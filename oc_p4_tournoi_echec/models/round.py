import json

class Round:
    def __init__(self, name: str, date: str, start_time: str, end_time: str, matches: list):
        self.name = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches

    @staticmethod
    def from_json(json_str: str) -> "Round":
        data = json.loads(json_str)
        return Round(**data)

    def to_json(self) -> str:
        data = self.__dict__.copy()
        return json.dumps(data)
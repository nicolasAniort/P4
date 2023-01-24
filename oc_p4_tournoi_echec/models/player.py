import datetime
import json

class Player:
    def __init__(self, last_name: str, first_name: str, birth_date: datetime.date, id: str) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.id = id
        self.points = 0
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.id})\nPoints: {self.points}'
        
    @staticmethod
    def from_json(json_str: str) -> 'Player':
        data = json.loads(json_str)
        return Player(**data)

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
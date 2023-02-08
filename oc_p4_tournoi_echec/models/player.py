import datetime
import json

class Player:
    
    """ initialisation du constructeur de classe"""
    def __init__(self, last_name: str, first_name: str, birth_date: datetime.date, national_id: str, score: int):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.score = score       
    
    """Elle permet de définir comment l'objet doit s'afficher sous forme de chaîne de caractères. 
    Dans cette classe, elle renvoie une chaîne de caractères formatée avec les informations de l'objet."""
    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.birth_date} {self.national_id}{self.score}\n'
        
    @staticmethod
        
    def from_json(json_str: str) -> 'Player':
        data = json.loads(json_str)
        return Player(**data)
        #La méthode from_json prend en entrée une chaîne de caractères JSON et utilise la bibliothèque
        #json de Python pour la désérialiser en un objet Player en utilisant l'opérateur ** pour passer 
        #les propriétés déserialisées en tant qu'arguments à la méthode __init__"""
    
    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        #La méthode to_json prend l'objet Player en entrée et utilise la bibliothèque json de Python pour 
        #le sérialiser en une chaîne de caractères JSON en utilisant les valeurs des propriétés de l'objet.
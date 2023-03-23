from ast import List


class Player():
    
    """ initialisation du constructeur de joueur (moule)"""
    def __init__(self, last_name: str, first_name: str, birth_date: str, national_id: str, rank: int, adversary:List):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.rank = rank
        self.adversary = adversary
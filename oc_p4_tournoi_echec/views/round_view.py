from models.round import Round

class RoundView:
    def __init__(self, round:Round):
        self.round = round

    def list(self) -> str:
        """Affiche la liste des matchs d'un tour."""
        result = ''
        for match in self.round.matches:
            result += f'{match}\n'
        return result

    def get(self, id:int) -> str:
        """Affiche le match d'un tour avec l'identifiant donné."""
        result = ''
        for match in self.round.matches:
            if match.id == id:
                result += f'{match}\n'
        return result
class Round:
    def __init__(self, name, start_time=None, end_time=None, matches=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def __repr__(self):
        return f"<Round {self.name} ({len(self.matches)} matches)>"
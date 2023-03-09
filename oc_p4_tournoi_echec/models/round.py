class Round:
    def __init__(self, name, start_time=None, end_time=None, matches=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = []

    
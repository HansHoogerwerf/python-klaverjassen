class Player:
    def __init__(self, name):
        self.name = name
        self.hand = None
        self.team = None

    def set_team(self, team):
        self.team = team

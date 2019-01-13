class Team:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        player1.set_team(self)
        player2.set_team(self)

        self.points = 0
        self.challengers = False

    def set_challengers(self):
        self.challengers = True

    def add_to_points(self, points):
        self.points += points

    def has_player(self, player):
        return self.player1 is player or self.player2 is player

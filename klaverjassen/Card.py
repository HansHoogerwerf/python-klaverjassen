class Card:
    def __init__(self, value, color, points):
        self.value = value
        self.color = color
        self.points = points
        self.trump = False
        self.allowed = False

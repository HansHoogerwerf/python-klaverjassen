import Player


class RandomPlayer(Player.Player):
    def __init__(self):
        super().__init__()

    def choose_card(self, game, turn):
        for card in self.hand:
            if card.allowed:
                return card
        return None

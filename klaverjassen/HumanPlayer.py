import Player


class HumanPlayer(Player.Player):
    def __init__(self):
        super().__init__()

# TODO implement a human readable way of choosing a card
    def choose_card(self, game, turn):
        for card in self.hand:
            if card.allowed:
                return card
        return None

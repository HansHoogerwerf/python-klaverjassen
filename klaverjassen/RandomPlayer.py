import Player
from random import random


class RandomPlayer(Player.Player):
    def __init__(self, name):
        super().__init__(name)

    def challenge_hand(self, game):
        r = random()
        # Using this method the North player is way more likely to play than the others,
        # with the west player on the lowest end of the scale.
        # However this does not matter as the other things like
        # the players, cards and start player are completely random.
        return r > 0.75

    def choose_card(self, game, turn):
        for card in self.hand:
            if card.allowed:
                return card
        return None

    # Do nothing with the hand result
    def hand_result(self, turn):
        return

    # Do nothing with the game result
    def game_result(self, game):
        return

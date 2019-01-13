import Player
from random import random


# http://games.basicflow.net/klaverjas/ai.js
class Playable:
    def __init__(self, name):
        self.max = []
        self.min = []
        self.diff = []
        self.mean = []
        self.risk = []

    def add_new_card(self, card):
        self.max.append(card)
        self.min.append(card)
        self.diff.append(card)
        self.mean.append(card)
        self.risk.append(card)


class RandomPlayer(Player.Player):


    def __init__(self, name):
        super().__init__(name)

    def challenge_hand(self):
        r = random()
        # Using this method the North player is way more likely to play than the others,
        # with the west player on the lowest end of the scale.
        # However this does not matter as the other things like
        # the players, cards and start player are completely random.
        return r > 0.75

    def choose_card(self, game, turn):
        # Setup the playable cards and other info
        playable = Playable()
        allowed_cards = []
        for card in self.hand:
            if card.allowed:
                playable.add_new_card(card)
        trump = game.trump
        firstPlayer = turn.start_player



        return None

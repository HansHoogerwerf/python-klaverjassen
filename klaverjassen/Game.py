from random import shuffle, choice

import util
from Card import Card
from PackOfCards import values, colors
from Turn import Turn


class Game:
    def __init__(self, players):
        self.players = players
        self.trump = choice(colors)
        self.turns = []
        self.total_points = 0
        create_hands(self.trump, self.players)

    def play_game(self):
        start_player = self.players[0]
        for i in range(0, 8):
            turn = self.play_turn(start_player)
            self.total_points += turn.points
            start_player = turn.winner

        if self.players[0].points <= self.players[1].points:
            self.players[1].points += self.players[0].points
            self.players[3].points += self.players[0].points
            self.players[0].points = 0
            self.players[2].points = 0

        return self

    def reshuffle(self):
        create_hands(self.trump, self.players)

    def play_turn(self, start_player):
        turn = Turn(start_player)
        self.turns.append(turn)
        start_player_position = self.players.index(start_player)

        for i in range(0, 4):
            player = self.players[(i + start_player_position) % 4]
            set_possibilities(turn, player)
            card = player.choose_card(self, turn)
            player.hand.remove(card)
            reset_possibilities(player)
            turn.play_card(player, card)
        turn.calculate_turn_points()
        turn.turn_winner()

        return turn


def create_deck():
    deck_of_cards = []
    for value in values:
        for color in colors:
            deck_of_cards.append(Card(value[0], color, value[1]))
    return deck_of_cards


def create_hands(trump_color, players):
    deck_of_cards = create_deck()
    shuffle(deck_of_cards)
    set_trump(deck_of_cards, trump_color)
    for i in range(0, len(players)):
        players[i].hand = deck_of_cards[i * 8:(i + 1) * 8]


def set_trump(deck_of_cards, trump):
    for card in deck_of_cards:
        if card.color is trump:
            card.trump = True
            if card.value is '9':
                card.points = 14
            if card.value is 'boer':
                card.points = 20


def set_possibilities(turn, player):
    util.check_possibilities(turn, player.hand)


def reset_possibilities(player):
    util.reset_possibilities(player)

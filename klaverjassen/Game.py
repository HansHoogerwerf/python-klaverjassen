from random import shuffle, choice
from Team import Team
import util
from Card import Card
from Deck import values, colors
from Turn import Turn


class Game:
    def __init__(self, players):
        self.players = players
        self.trump = choice(colors)
        self.turns = []
        self.total_points = 0
        self.teams = [Team(players[0], players[2]), Team(players[1], players[3])]
        create_hands(self.trump, self.players)

    def play_game(self, start_player):
        challenger = None

        while challenger is None:
            challenger = find_challenger(self)
            if challenger is None:
                self.reshuffle()
            else:
                challenger.team.challengers = True

        # if someone is challenging,  go play the hands
        for i in range(0, 8):
            turn = self.play_turn(start_player, i)
            # add points to team

            turn.winner.team.points += turn.points

            self.total_points += turn.points
            start_player = turn.winner

        # Calculate the score after a game. If the challenger team lost in points,
        # all the points go to the non-challenger team.
        # If the challenging team got all the points, give them 100 bonus points.

        for i in range(0, len(self.teams)):
            # Other team index
            j = (i + 1) % 2
            if self.teams[i].challengers and self.teams[j].points is 0:
                self.teams[i].points += 100
                break
            elif self.teams[i].challengers and self.teams[i].points <= self.teams[j].points:
                self.teams[j].points += self.teams[i].points
                self.teams[i].points = 0
                break
        return self

    def reshuffle(self):
        self.trump = choice(colors)
        create_hands(self.trump, self.players)

    def play_turn(self, start_player, turn_number):
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
        turn.calculate_turn_points(turn_number)
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


def find_challenger(game):
    for player in game.players:
        if player.challenge_hand():
            return player
    return None

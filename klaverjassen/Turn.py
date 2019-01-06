from PackOfCards import roem_order
from util import check_trump, get_highest_trump_card, get_highest_card_color, check_card


class Turn:
    def __init__(self, start_player):
        self.start_player = start_player
        self.players = []
        self.cards = []
        self.points = 0
        self.winning_card = None
        self.winner = None

    def play_card(self, player, card):
        self.players.append(player)
        self.cards.append(card)

    def calculate_turn_points(self):
        self.points = calculate_turn_points(self)
        return self.points

    def turn_winner(self):
        self.winning_card = winning_card(self)
        self.winner = self.players[self.cards.index(self.winning_card)]
        self.winner.points += self.points
        self.players[(self.players.index(self.winner) + 2) % 4].points += self.points


def calculate_turn_points(turn):
    points = 0
    for card in turn.cards:
        points += card.points
    points += calculate_roem_points(turn)
    return points


def calculate_roem_points(turn):
    # Total amount of roem
    roem = 0

    for card in turn.cards:
        # Start counting for cards in a row from the next card's index
        roem_order_index = roem_order.index(card.value) + 1
        roem_length = 1

        # If the next card is in the turn check for further cards until the streak stops
        while roem_order_index < 8 and check_card(turn.cards, roem_order[roem_order_index], card.color):
            roem_length += 1
            roem_order_index += 1

        # Add  the appropriate amount of roem for each streak
        if roem_length is 3:
            roem += 20
        if roem_length is 4:
            roem += 30

        # Implement the special rule for trump cards
        if card.trump and card.value is 'vrouw' and check_card(turn.cards, 'heer', card.color):
            roem += 20
    return roem


def winning_card(turn):
    if check_trump(turn.cards):
        return get_highest_trump_card(turn.cards)
    else:
        return get_highest_card_color(turn.cards, turn.cards[0].color)

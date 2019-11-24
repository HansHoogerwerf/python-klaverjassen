import Player


def pretty_print_card(card):
    print(card.color, card.value)


class HumanPlayer(Player.Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_card(self, game, turn):
        print("\nTrump color:", game.trump)

        if self.team.challengers:
            print("You are the challenger!")
        else:
            print("The opponents are the challengers!")

        print("Start player")
        print(turn.start_player.name)
        print("Cards played in this turn:")
        for card in turn.cards:
            pretty_print_card(card)

        allowed_cards = []
        for card in self.hand:
            if card.allowed:
                allowed_cards.append(card)
                print("Card number =", len(allowed_cards))
                pretty_print_card(card)

        try:
            card_id = int(input("Choose a card number presented above"))
            if card_id < 1 or card_id > len(allowed_cards):
                print("Pick a card within the bounds presented!")
                return self.choose_card(game, turn)
            else:
                return allowed_cards[card_id - 1]
        except:
            print("An exception occured when choosing a card, try again.")
            return self.choose_card(game, turn)

        return None

    def challenge_hand(self, game):
        # Give the player information
        print("Trump:", game.trump)

        for card in self.hand:
            pretty_print_card(card)

        # ask the player if the hand is played
        return input("Press Y to play the hand, N to not play this hand.").lower() == 'y'

    def hand_result(self, turn):
        print("Winner:", turn.winner.name)
        print("Points:", turn.points)

        print("Cards played: ")
        for card in turn.cards:
            pretty_print_card(card)

    def game_result(self, game):
        for team in game.teams:
            print("Team points:", team.player1.name, team.player2.name, team.points)

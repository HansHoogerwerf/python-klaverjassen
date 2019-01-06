from PackOfCards import trump_order, normal_order


def check_color(cards, color):
    for card in cards:
        if card.color is color:
            return True
    return


def check_trump(cards):
    for card in cards:
        if card.trump:
            return True
    return False


def check_card(cards, value, color):
    if value is None:
        return False
    for card in cards:
        if card.value is value and card.color is color:
            return True
    return False


def get_highest_trump_card(cards):
    highest_trump_index = -1
    highest_trump_card = None
    for card in cards:
        if card.trump and card.allowed:
            trump_index = trump_order.index(card.value)
            if trump_index > highest_trump_index:
                highest_trump_index = trump_index
                highest_trump_card = card
    return highest_trump_card


def get_highest_card_color(cards, color):
    highest_index = -1
    highest_card = None
    for card in cards:
        if card.allowed and card.color is color:
            index = normal_order.index(card.value)
            if index > highest_index:
                highest_index = index
                highest_card = card
    return highest_card


def check_trump_possibilities(turn, hand):
    for card in hand:
        card.allowed = card.trump

    # Check the highest trump card
    highest_trump_index_hand = -1
    highest_trump_index_turn = -1

    trump_hand = check_trump(hand)

    trump_turn = check_trump(turn.cards)

    if trump_hand:
        highest_trump_index_hand = trump_order.index(get_highest_trump_card(hand).value)

    if trump_turn:
        highest_trump_index_turn = trump_order.index(get_highest_trump_card(turn.cards).value)

    # If the hand has a card with a bigger trump card set the allow to cards higher than the highest turn trump card
    if highest_trump_index_hand > highest_trump_index_turn:
        for card in hand:
            if card.allowed:
                card.allowed = trump_order.index(card.value) > highest_trump_index_turn


def check_possibilities(turn, hand):
    # Is list empty, then we are the first and we allow everything
    if not turn.cards:
        for card in hand:
            card.allowed = True
        return
    first_card = turn.cards[0]

    # Check if we have the color, if we do we only allow the color and check for trump cards
    if check_color(hand, first_card.color):
        if first_card.trump:
            check_trump_possibilities(turn, hand)
        else:
            for card in hand:
                if card.color is first_card.color:
                    card.allowed = True
        return

    # Check if we have trump cards, if we do we only allow trump cards higher than the trump cards already played
    if check_trump(hand):
        check_trump_possibilities(turn, hand)
        return

    # Otherwise allow everything again
    for card in hand:
        card.allowed = True
    return


def select_random_possibility(hand):
    for card in hand:
        if card.allowed:
            return card
    return None


def reset_possibilities(player):
    for card in player.hand:
        card.allowed = False

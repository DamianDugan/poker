def map_hands_to_list(hands):
    hands_list = [hands[i:i + 2] for i in range(0, len(hands), 3)]
    return hands_list


def split_list(hands_list):
    half = len(hands_list)//2
    return hands_list[:half], hands_list[half:]


# Deprecated function, no need for merging list
# def merge_hands(hand_one, hand_two):
#     return hand_one + hand_two


# Deprecated function, found another solution
# def indices(hand, value):
#     return [i for i, x in enumerate(hand) if x == value]


def add_weight_to_cards(hand):
    weighted_hands = []
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    for card in hand:
        for value in values:
            if card[0] == value:
                weighted_hands.append(values.index(value))

    return weighted_hands


def strip_colours(hand):
    colourless_hand = []
    for card in hand:
        colourless_hand.append(card[0])

    return colourless_hand


def get_colours(hand):
    colourful_hand = []
    for card in hand:
        colourful_hand.append(card[1])
    return colourful_hand


def remove_values_from_list(hand, val):
    return [value for value in hand if value != val]


def is_straight_flush(hand):
    if is_straight(hand) and is_flush(hand):
        return True
    return False


def is_four_of_a_kind(hand):
    colourless_hand = strip_colours(hand)
    for card in colourless_hand:
        if colourless_hand.count(card) is 4:
            return True
    return False


def is_full_house(hand):
    # I should have used a dict...
    colourless_hand = strip_colours(hand)
    reduced_hand = []
    for card in colourless_hand:
        if colourless_hand.count(card) is 3:
            reduced_hand = remove_values_from_list(colourless_hand, card)

    if len(reduced_hand) is not 0:
        for card in reduced_hand:
            if reduced_hand.count(card) is 2:
                return True
    return False


def is_flush(hand):
    colourful_hand = get_colours(hand)
    if colourful_hand.count(colourful_hand[0]) is 5:
        return True
    return False


def is_straight(hand):
    weighted_colourless_hand = add_weight_to_cards(hand)
    weighted_colourless_hand.sort()
    n = weighted_colourless_hand

    # I'm tired, sorry about this bit of code
    if n[0] + 1 == n[1] and n[1] + 1 == n[2] and n[2] + 1 == n[3] and n[3] + 1 == n[4]:
        return True
    # Check for low A straight
    if n[0] + 1 == n[1] and n[1] + 1 == n[2] and n[2] + 1 == n[3] and n[3] + 9 == n[4]:
        return True
    return False


def is_three_of_a_kind(hand):
    colourless_hand = strip_colours(hand)
    for card in colourless_hand:
        if colourless_hand.count(card) is 3:
            return True
    return False


def is_two_pairs(hand):
    colourless_hand = strip_colours(hand)
    reduced_hand = []
    for card in colourless_hand:
        if colourless_hand.count(card) is 2:
            reduced_hand = remove_values_from_list(colourless_hand, card)

    if len(reduced_hand) is not 0:
        for card in reduced_hand:
            if reduced_hand.count(card) is 2:
                return True
    return False


def is_one_pair(hand):
    colourless_hand = strip_colours(hand)
    for card in colourless_hand:
        if colourless_hand.count(card) is 2:
            return True
    return False


def tie_breaker(player_one_hand, player_two_hand):
    # TODO :Check for edge cases where having the highest card does not make you win such as :
    # AS, AH, 2S, 2C, 2D vs KH, KS, KD, 3S, 3H
    weighted_player_one_hand = add_weight_to_cards(player_one_hand)
    weighted_player_two_hand = add_weight_to_cards(player_two_hand)

    if max(weighted_player_one_hand) > max(weighted_player_two_hand):
        return "player one"
    return "player two"


def add_weight_to_hand(hand):
    if is_straight_flush(hand):
        return 8
    if is_four_of_a_kind(hand):
        return 7
    if is_full_house(hand):
        return 6
    if is_flush(hand):
        return 5
    if is_straight(hand):
        return 4
    if is_three_of_a_kind(hand):
        return 3
    if is_two_pairs(hand):
        return 2
    if is_one_pair(hand):
        return 1
    return 0


def get_winner(player_one, player_two):
    weighted_player_one_hand = add_weight_to_hand(player_one)
    weighted_player_two_hand = add_weight_to_hand(player_two)
    victory_count = 0
    if weighted_player_one_hand > weighted_player_two_hand:
        victory_count += 1
    if weighted_player_one_hand is weighted_player_two_hand:
        if tie_breaker(player_one, player_two) is "player one":
            victory_count += 1

    return "Player 1 has won : ", victory_count, " games"


hand_list = map_hands_to_list("8H 2S 4S 3S 5S 4H TH 8H 6H AH")

player_one_hand, player_two_hand = (split_list(hand_list))

print(get_winner(player_one_hand, player_two_hand))
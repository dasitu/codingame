# https://www.codingame.com/multiplayer/bot-programming/fireworks

import sys
import random


def resolve_info(info):
    info_array = info.split(":")
    player_id = info_array[0]
    card_index = info_array[2]
    card = info_array[3]
    color = card.split("-")[0]
    level = card.split("-")[1]
    return player_id, card_index, card, color, level


def next_possible_card(current_board):
    candidates = []
    for color, levels in current_board.items():
        count = len(levels)
        if count < 5:
            candidates.append("{}-{}".format(color, count + 1))
    return candidates


def is_card_in_hand(card, hand):
    for index, c in hand.items():
        if card == c:
            return index
    return False


def safe_remove_list(mylist, value):
    if value in mylist:
        mylist.remove(value)
    return mylist


def update_hand_cards(player_id, card_index, card):
    color = card.split("-")[0]
    level = card.split("-")[1]
    my_card = hand_cards[player_id][card_index].split("-")
    if color != "?":
        my_card[0] = color
    if level != "?":
        my_card[1] = level
    hand_cards[player_id][card_index] = "{}-{}".format(my_card[0], my_card[1])


def determine_say_type(player_id, card_index):
    split_a = hand_cards[player_id][card_index].split("-")
    color = split_a[0]
    level = split_a[1]
    if level == "?":
        return "l"
    elif color == "?":
        return "c"
    return None


def determine_discard_card():
    # level 5 only have 1 card, should not be discard
    # the strategy is to discard by order
    # 1. Remove level 5
    # 2. known cards already in boards
    # 3. lower level first
    # 3. if still multiple remains, random select
    my_cards = hand_cards[my_id]
    discard_cards = my_cards.copy()
    for card_i, card in my_cards.items():
        if "5" in card:
            discard_cards.pop(card_i)
            continue
        color = card.split("-")[0]
        level = card.split("-")[1]
        if color != "?" and level in current_board[color]:
            return card_i
        if level == "1":
            return card_i
    rand_i = random.randint(0, len(discard_cards) - 1)
    return list(discard_cards.keys())[rand_i]


my_id = ""
current_board = {}  # {"RED":[1,2,3],"GREEN":[1,2],"YELLOW":[]}

# initial all cards and current_board
colors = ["GREEN", "YELLOW", "RED", "WHITE", "BLUE"]
levels = ["1", "1", "1", "2", "2", "3", "3", "4", "4", "5"]
cards = {}
for c in colors:
    cards[c] = levels.copy()
    current_board[c] = []

hand_cards = {"0": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"},
              "1": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"},
              "2": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"}
              }

seen_cards = {"0": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"},
              "1": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"},
              "2": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"}
              }

# game loop
while True:
    # remaining_possible_error: the number of possible PLAY error before loosing
    # remaining_possible_information: the number of possible SAY action
    remaining_possible_error, remaining_possible_information = [int(i) for i in input().split()]
    information_count = int(input())  # the number of information given during the last turn
    print(remaining_possible_error, remaining_possible_information, file=sys.stderr, flush=True)
    print(information_count, file=sys.stderr, flush=True)

    # processing the data and update customized data structure
    for i in range(information_count):
        info = input()  # one line of information (PLAY, DISCARD, ERROR, SAYLEVEL, SAYCOLOR or CARD)
        print(info, file=sys.stderr, flush=True)

        # these are the cards in other hand information, just update the seen_cards
        if i >= information_count - 10 and "CARD" in info:
            player_id, card_index, card, color, level = resolve_info(info)
            seen_cards[player_id][card_index] = card

        # 0:NEWGAME
        elif "NEWGAME" in info:
            my_id = info.split(":")[0]
            hand_cards = {"0": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"},
                          "1": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"},
                          "2": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"}
                          }
            seen_cards = {"0": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"},
                          "1": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"},
                          "2": {"A": "?-?", "B": "?-?", "C": "?-?", "D": "?-?", "E": "?-?"}
                          }
            for c in colors:
                cards[c] = levels.copy()
                current_board[c] = []

        elif "DISCARD" in info:
            player_id, card_index, card, color, level = resolve_info(info)
            safe_remove_list(cards[color], level)
            hand_cards[player_id][card_index] = "?-?"

        # 2:PLAY:A:RED-1
        elif "PLAY" in info:
            player_id, card_index, card, color, level = resolve_info(info)
            current_board[color].append(level)
            # already played
            hand_cards[player_id][card_index] = "?-?"

        # 1:CARD:B:YELLOW-3
        elif "CARD" in info:
            player_id, card_index, card, color, level = resolve_info(info)
            if color != "?" and level != "?":
                cards[color] = safe_remove_list(cards[color], level)
            update_hand_cards(player_id, card_index, card)

        # 0:ERROR:A:WHITE-4
        elif "ERROR" in info:
            player_id, card_index, card, color, level = resolve_info(info)
            safe_remove_list(cards[color], level)
            hand_cards[player_id][card_index] = "?-?"

    next_cards = next_possible_card(current_board)
    print("current_board:", current_board, file=sys.stderr, flush=True)
    print("hand_cards:", hand_cards, file=sys.stderr, flush=True)
    print("seen_cards:", seen_cards, file=sys.stderr, flush=True)
    print("next_possible_card:", next_cards, file=sys.stderr, flush=True)

    complete_command = False
    output = ""
    for card in next_cards:
        # card in my hand, then play
        index = is_card_in_hand(card, hand_cards[my_id])
        if index:
            output = "PLAY:{}".format(index)
            break

        # card in others hand, say
        for player_id, player_card in seen_cards.items():
            card_index = is_card_in_hand(card, player_card)
            if card_index and remaining_possible_information > 0:
                t = determine_say_type(player_id, card_index)
                if t == "l":
                    say_type = card.split("-")[1]
                    output = "SAY:{}:{}".format(player_id, say_type)
                    complete_command = True
                    break
                elif t == "c":
                    say_type = card.split("-")[0]
                    output = "SAY:{}:{}".format(player_id, say_type)
                    complete_command = True
                    break
                else:
                    continue

        if complete_command:
            break

    if output == "":
        index = determine_discard_card()
        output = "DISCARD:{}".format(index)

    print(output)

# https://www.codingame.com/ide/puzzle/codingame-sponsored-contest
import sys
import math


def get_distance(pos1, pos2):
    distance = math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2)
    print("{}{}:{}".format(pos1, pos2, distance), file=sys.stderr)
    return distance


def get_closest_player(my_pos, others_pos):
    min_distance = 99999999
    nearest_pos = ()
    for pos in others_pos:
        distance = get_distance(my_pos, pos)
        if distance < min_distance:
            nearest_pos = pos
            min_distance = distance
    return nearest_pos


def get_all_next_pos(players_pos):
    p = [1, -1]
    all_pos = []
    for pos in players_pos:
        for index, value in enumerate(pos):
            for v in p:
                new_pos = list(pos)
                new_pos[index] = value + v
                all_pos.append(tuple(new_pos))
    # print("All possible pos:{}".format(all_pos), file=sys.stderr)
    return all_pos


def get_next_pos(pos, direction):
    col_delta = row_delta = 0
    if direction == "left":
        col_delta = -1
    elif direction == "right":
        col_delta = 1
    elif direction == "up":
        row_delta = -1
    else:
        row_delta = 1
    new_row = pos[0] + row_delta
    new_col = pos[1] + col_delta
    return new_row, new_col


col_num = int(input())
row_num = int(input())
players_num = int(input())
print("{} {} {}".format(col_num, row_num, players_num), file=sys.stderr)
direct_sequence = ["left", "down", "right", "up"]
command_map = {"left": "C", "down": "A", "right": "D", "up": "E", "still": "B"}
my_foot_print = []

# game loop
while True:
    players_pos = []
    my_pos = ()

    # decode allowed directions
    allowed_directions = []
    for i in range(4):
        input_direction = input()
        if input_direction == "_":
            allowed_directions.append(direct_sequence[i])
    print(allowed_directions, file=sys.stderr)

    # add players data to defined variable
    for i in range(players_num):
        row, col = [int(j) for j in input().split()]
        players_pos.append((row, col))
    my_pos = players_pos.pop()
    my_foot_print.append(my_pos)
    print(players_pos, file=sys.stderr)
    print(my_pos, file=sys.stderr)

    # start to calculate what is the next step
    closest_player = get_closest_player(my_pos, players_pos)  # used by the longest distance strategy
    longest_distance = 1                                      # used by the longest distance strategy
    longest_direction = ""                                    # used by the longest distance strategy
    next_move = "still"     # if all strategy are not valid, keep still
    candidate_directions = []  # every strategy have its own weights, final selection based on the weights
    all_possible_pos = get_all_next_pos(players_pos)    # used to check whether next move will conflict with others

    # start to check every direction
    for d in allowed_directions:
        print("checking:{}".format(d), file=sys.stderr)
        candidate_directions.append(d)

        # calculate new pos for current direction
        new_row, new_col = get_next_pos(my_pos, d)

        # just skip it since this will cause end of the game
        if (new_row, new_col) in all_possible_pos:
            print("conflict!", file=sys.stderr)
            candidate_directions.remove(d)
            continue

        if (new_row, new_col) not in my_foot_print:
            distance_to_new_pos = get_distance(closest_player, (new_row, new_col))
            if distance_to_new_pos > longest_distance:
                longest_direction = d
                longest_distance = distance_to_new_pos
        else:
            print("in foot_print!", file=sys.stderr)

    print("longest_direction:{}".format(longest_direction), file=sys.stderr)

    # just use longest_direction
    next_move = longest_direction if longest_direction != "" else next_move

    # no longest_direction but still have some valid direction
    if len(candidate_directions) > 0 and next_move == "still":
        next_move = candidate_directions[0]

    print(next_move, file=sys.stderr)
    print(command_map[next_move])

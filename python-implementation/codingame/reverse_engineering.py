# https://www.codingame.com/ide/puzzle/codingame-sponsored-contest
import sys
import math


def cal_distance(pos1, pos2):
    distance = math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2)
    return distance


def find_closest_player(my_pos, others_pos):
    min_distance = 99999999
    nearest_pos = ()
    for pos in others_pos:
        distance = cal_distance(my_pos, pos)
        if distance < min_distance:
            nearest_pos = pos
            min_distance = distance
    return nearest_pos


I = input
row_count = int(I())
col_count = int(I())
player_count = int(I())

print("{} {} {}".format(row_count, col_count, player_count), file=sys.stderr)

direct_sequence = ["left", "down", "right", "up"]
command_map = {"left": "C",
               "down": "A",
               "right": "D",
               "up": "E",
               "still": "B"}

my_foot_print = []

# game loop
while True:
    players_pos = []
    my_pos = ()
    allowed_directions = [I(), I(), I(), I()]
    print(allowed_directions, file=sys.stderr)

    for index, direct in enumerate(allowed_directions):
        if direct == "_":
            allowed_directions[index] = direct_sequence[index]

    allowed_directions = list(filter(lambda a: a != "#", allowed_directions))
    print(allowed_directions, file=sys.stderr)

    for i in range(player_count):
        row, col = [int(j) for j in input().split()]
        if i == player_count - 1:
            my_pos = (row, col)
            my_foot_print.append(my_pos)
        else:
            players_pos.append((row, col))
    print(players_pos, file=sys.stderr)
    print(my_pos, file=sys.stderr)

    closest_player = find_closest_player(my_pos, players_pos)
    longest_distance = 0
    next_move = "still"

    for d in allowed_directions:
        col_delta = row_delta = 0
        if d == "left":
            col_delta = -1
        elif d == "right":
            col_delta = 1
        elif d == "up":
            row_delta = -1
        else:
            row_delta = 1
        new_row = my_pos[0] + row_delta
        new_col = my_pos[1] + col_delta
        if (new_row, new_col) in players_pos or (new_row, new_col) in my_foot_print:
            if d in allowed_directions:
                allowed_directions.remove(d)
                continue

        distance_to_new_pos = cal_distance(my_pos, (new_row, new_col))
        if distance_to_new_pos > longest_distance:
            next_move = d
            longest_distance = distance_to_new_pos

    if len(allowed_directions) > 0 and next_move == "still":
        next_move = allowed_directions[0]
    print(command_map[next_move])

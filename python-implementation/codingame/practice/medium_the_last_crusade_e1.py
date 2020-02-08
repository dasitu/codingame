import sys

room_types = {0: [()],
              1: {"TOP": "DOWN", "LEFT": "DOWN", "RIGHT": "DOWN"},
              2: {"LEFT": "RIGHT", "RIGHT": "LEFT"},
              3: {"TOP": "DOWN"},
              4: {"TOP": "LEFT", "RIGHT": "DOWN"},
              5: {"TOP": "RIGHT", "LEFT": "DOWN"},
              6: {"LEFT": "RIGHT", "RIGHT": "LEFT"},
              7: {"TOP": "DOWN", "RIGHT": "DOWN"},
              8: {"LEFT": "DOWN", "RIGHT": "DOWN"},
              9: {"LEFT": "DOWN", "TOP": "DOWN"},
              10: {"TOP": "LEFT"},
              11: {"TOP": "RIGHT"},
              12: {"RIGHT": "DOWN"},
              13: {"LEFT": "DOWN"}}


def get_next_pos(current, from_direction, room_int_type):
    x, y = current
    room_options = room_types[room_int_type]
    print("room_options:", room_options, file=sys.stderr)
    to_direction = room_options[from_direction]
    if to_direction == "DOWN":
        y += 1
    elif to_direction == "LEFT":
        x -= 1
    elif to_direction == "RIGHT":
        x += 1
    return x, y


grid = {}
# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
print("width:{} height:{}".format(w, h), file=sys.stderr)
for row in range(h):
    # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    types_in_col = input().split(" ")
    # print(types_in_col, file=sys.stderr)
    for col, room_type in enumerate(types_in_col):
        grid[(col, row)] = int(room_type)
        print("({},{}):{}".format(col, row, room_type), file=sys.stderr)
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
print(ex, file=sys.stderr)

# game loop
while True:
    icol, irow, pos = input().split()
    print("{} {} {}".format(icol, irow, pos), file=sys.stderr)
    current_pos = int(icol), int(irow)
    print("room_type:", grid[current_pos], file=sys.stderr)
    next_x, next_y = get_next_pos(current_pos, pos, grid[current_pos])

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print("{} {}".format(next_x, next_y))

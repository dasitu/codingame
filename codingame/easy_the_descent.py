import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    mountain = {}
    for i in range(8):
        mountain[i] = int(input())  # represents the height of one mountain.

    sorted_mountain = dict(sorted(mountain.items(), key=lambda x: x[1], reverse=True))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(list(sorted_mountain.keys())[0])
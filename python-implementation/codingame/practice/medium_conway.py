# https://www.codingame.com/ide/puzzle/conway-sequence

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
l = int(input())

last_list = [r]
output = []

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for i in range(l-1):
    temp_list = []
    last_value = 0
    last_count = 0
    for v in last_list:
        if last_value == 0:
            last_value = v
            last_count = 1
        elif v == last_value:
            last_count += 1
        else:
            temp_list.extend([last_count, last_value])
            last_value = v
            last_count = 1
    temp_list.extend([last_count, last_value])
    last_list = temp_list
    print("round:{} = {}".format(i, last_list), file=sys.stderr)

print(*last_list)
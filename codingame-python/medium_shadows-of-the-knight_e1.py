import sys
import math

def print_debug(msg):
    print(msg, file=sys.stderr)
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

print_debug('building:({},{})'.format(w,h))
print_debug('jumps left:{}'.format(n))
print_debug('starting:({},{})'.format(x0,y0))


w_max = w
w_min = 0
h_max = h
h_min = 0
w_range = [w_min, w_max]
h_range = [h_min, h_max]

# game loop
while True:
    bomb_dir = list(input())  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print_debug(bomb_dir)

    if 'U' in bomb_dir:
        h_range = [h_min, y0]
        h_max = y0
    if 'D' in bomb_dir:
        h_range = [y0, h_max]
        h_min = y0
    if 'R' in bomb_dir:
        w_range = [x0, w_max]
        w_min = x0
    if 'L' in bomb_dir:
        w_range = [w_min, x0]
        w_max = x0

    next_w = int(sum(w_range)/2)
    next_h = int(sum(h_range)/2)
    print_debug('range is w:{}, h:{}'.format(w_range, h_range))
    x0, y0 = next_w, next_h
    # the location of the next window Batman should jump to.
    print("{} {}".format(next_w, next_h))
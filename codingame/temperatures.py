import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

closest = 5527
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    print("closest:{}, input:{}".format(closest,t), file=sys.stderr)
    if t == closest:
        continue
    if abs(t) < abs(closest):
        closest = t
    elif abs(t) == abs(closest):
        closest = abs(t)

if closest == 5527:
    closest = 0

print(closest)
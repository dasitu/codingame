import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

meme_str = input()

meme_strs = re.sub(r'\W+', '', meme_str)
meme_strs = "".join(set(meme_strs))
sum_value = 0
for c in meme_strs:
    sum_value += ord(c)

output = sum_value % len(meme_str)

if output > 10:
    output = 10

print(meme_strs, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(str(output)+'/10')
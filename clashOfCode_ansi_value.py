import sys
import re

meme_str = input()
#meme_str = 'ha cse'
meme_strs = re.sub(r'\W+', '', meme_str)
meme_strs = "".join(set(meme_strs))
sum_value = 0
output = 0
for c in meme_strs:
    sum_value += ord(c)
output = 10 if output > 10 else sum_value % len(meme_str)
print(meme_strs, file=sys.stderr)
print(str(output)+'/10')
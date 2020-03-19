# https://www.codingame.com/ide/puzzle/scrabble

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def get_score(letter):
    scores = [
        ("eaionrtlsu", 1),
        ("dg", 2),
        ("bcmp", 3),
        ("fhvwy", 4),
        ("k", 5),
        ("jx", 8),
        ("qz", 10),
            ]
    for chars, v in scores:
        if letter in chars:
            return v


n = int(input())
words = []
for i in range(n):
    words.append(input())
letters = input()

biggest_point = 0
word = ""

for w in words:
    print("checking {}".format(w), file=sys.stderr)

    skip = False
    total = 0
    temp_letters = letters
    for c in w:
        if c not in temp_letters:
            total = 0
            skip = True
            break
        else:
            total += get_score(c)
            index_l = temp_letters.index(c)
            temp_letters = temp_letters[:index_l] + temp_letters[index_l+1:]
    print("total={}".format(total), file=sys.stderr)

    if skip:
        continue

    if total > biggest_point:
        biggest_point = total
        word = w

    print("current:{}, {}".format(word, biggest_point), file=sys.stderr)

print(word)

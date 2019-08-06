# For all possible radixes (from 2 to 16 inclusive),
# if the given string is a valid representation for one of this radix,
# you should print the radix followed by the decimal conversion of the given string using this radix.
#
# Example:
# input:
# f
# output:
# 16 15
#
# input:
# 1e
# output:
# 15 29
# 16 30
#
# input:
# 1
# output:
# 2 1
# 3 1
# 4 1
# 5 1
# 6 1
# 7 1
# 8 1
# 9 1
# 10 1
# 11 1
# 12 1
# 13 1
# 14 1
# 15 1
# 16 1
#
# input:
# e
# output:
# 15 14
# 16 14
#
# input:
# ffff
# output:
# 16 65535

# ascii code
# a=97, f=102
# 1=49, 9=57

x = input()
for i in range(2, 17):
    sumV = 0
    valid = True
    for e, j in enumerate(reversed(x)):
        if ord(j) > 102 - (16 - i):
            valid = False
            break
        elif ord(j) >= 97:
            j = ord(j) - 97 + 10
        else:
            j = int(j)
        sumV += j * i**e
    if valid:
        print("{} {}".format(i, int(sumV)))

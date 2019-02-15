import sys
import math


def cal_next(r: list) -> list:
    last = r[-1]
    for d in str(last):
        last += int(d)
    r.append(last)
    return r


r_1 = [int(input())]
r_2 = [int(input())]

while r_1[-1] != r_2[-1]:
    if r_1[-1] > r_2[-1]:
        r_2 = cal_next(r_2)
    else:
        r_1 = cal_next(r_1)
    # print("r1:{}".format(r_1), file=sys.stderr)
    # print("r2:{}".format(r_2), file=sys.stderr)

print(r_1[-1])

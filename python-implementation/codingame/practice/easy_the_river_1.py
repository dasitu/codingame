import sys


def cal_next(r: int) -> int:
    for d in str(r):
        r += int(d)
    return r


# r_1 = int(input())
# r_2 = int(input())
r_1 = 32
r_2 = 47
while r_1 != r_2:
    if r_1 > r_2:
        r_2 = cal_next(r_2)
    else:
        r_1 = cal_next(r_1)
    print("r1:{}".format(r_1), file=sys.stderr)
    print("r2:{}".format(r_2), file=sys.stderr)

print(r_1)

import math


def can_be_draw_using_geometric_construction(n):
    fermat_primes = [1, 3, 5, 17, 257, 65537]
    for f in fermat_primes:
        d = n / f
        power = 0
        while d >= math.pow(2, power):
            if d == math.pow(2, power):
                return True
            power += 1
    return False


a, b = [int(i) for i in input().split()]
count = 0
for i in range(a, b + 1):
    if can_be_draw_using_geometric_construction(i):
        count += 1

print(count)

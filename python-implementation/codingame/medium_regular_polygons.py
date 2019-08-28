import math


def can_be_draw_using_geometric_construction(n):
    fermat_primes = [3, 5, 17, 257, 65537]
    for f in fermat_primes:
        if n % f == 0:
            n = n // f
    if math.log(n, 2).is_integer():
        return True
    return False


a, b = [int(i) for i in input().split()]
count = 0
for i in range(a, b + 1):
    if can_be_draw_using_geometric_construction(i):
        count += 1

print(count)
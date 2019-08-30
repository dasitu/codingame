import math
from itertools import combinations


def count_of_regular_polygons(n):
    result = 1
    fermat_primes = [3, 5, 17, 257, 65537]

    # formulate all combinations of fermat_primes
    combination_values = fermat_primes[:]
    for i in range(2, len(fermat_primes)+1):
        all_combination = list(combinations(fermat_primes, i))
        # print(all_combination)
        for combination in all_combination:
            value = 1
            for v in combination:
                value *= v
            combination_values.append(value)
    combination_values.sort()
    # print(combination_values)

    # for every possible values, check log2(n/f) and fermat itself(log2(n/f)==0)
    for f in combination_values:
        if f <= n:
            result += math.floor(math.log2(n/f)) + 1  # additional 1 due to fermat itself, or log2(n/f) == 0
        else:
            break

    # for log2(n) itself
    result += math.floor(math.log2(n))
    return result


def can_be_draw_using_geometric_construction(n):
    fermat_primes = [3, 5, 17, 257, 65537]
    for f in fermat_primes:
        if n % f == 0:
            n = n // f
    if math.log(n, 2).is_integer():
        return True
    return False


a, b = [int(i) for i in input().split()]
count = count_of_regular_polygons(b) - count_of_regular_polygons(a)
if can_be_draw_using_geometric_construction(a):
    count += 1
print(count)
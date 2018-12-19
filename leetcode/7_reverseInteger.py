def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    import math
    max_num = math.pow(2,31) - 1
    minus = -1 if x < 0 else 1
    x = str(abs(x))
    x = int(x[::-1])
    x = x * minus if x < max_num else 0
    return x

print(reverse(1534236469))
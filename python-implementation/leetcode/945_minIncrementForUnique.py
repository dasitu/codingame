def minIncrementForUnique(A):
    """
    :type A: List[int]
    :rtype: int
    """
    count = 0
    uniqe_values = []
    dup_values = []
    for v in A:
        if v in uniqe_values:
            dup_values.append(v)
        else:
            uniqe_values.append(v)

    for value in sorted(dup_values):
        j = 1
        new_value = value
        while j < len(A):
            new_value = value + j
            if new_value not in uniqe_values:
                break
            j += 1
        count += new_value - value
        uniqe_values.append(new_value)
    return count

A = [3,2,1,2,1,7]
A = [1,2,2]
A = [1,3,0,3,0]
print(minIncrementForUnique(A))
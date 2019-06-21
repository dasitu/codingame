def maxSumAfterPartitioning(A, K):
    sorted_A = A.sort()
    visited_nodes = []

    for current_max in sorted_A:
        index = A.index(current_max)

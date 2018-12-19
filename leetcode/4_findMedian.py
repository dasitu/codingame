def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    added = sorted(nums1 + nums2)
    added_len = len(added)
    half = added_len // 2
    median = 0
    if added_len % 2:
        median = added[half]
    else:
        median = 0.5 * (added[half] + added[half-1])
    return median

print(findMedianSortedArrays([1,2],[3,4]))
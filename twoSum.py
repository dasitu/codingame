def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index1 in range(len(nums)):
        searched_num = target - nums[index1]
        if searched_num in nums:
            index2 = nums.index(searched_num)
            if index1 != index2:
                break
    return [index1, index2]


print(twoSum([2, 7, 11, 15], 9))

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x >= 0:
        x = str(x)
        if x == x[::-1]:
            return True
    return False
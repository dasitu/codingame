def isPalindrome(s):
    reversed_s = s[::-1]
    if s == reversed_s:
        return True
    return False

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    s_len = len(s)
    if s_len < 2:
        return s
    cur_len = s_len
    while cur_len <= s_len:
        left_index = 0
        while left_index <= s_len-cur_len:
            right_index = left_index + cur_len
            candidate = s[left_index:right_index]
            if candidate == candidate[::-1]:
                return candidate
            left_index += 1
        cur_len -= 1

def main():
    testcases = ['ac', 'bb', "babad", ' ', 'au', 'abbbabbb', 'abcabcbb', 'aaaa', 'abcabcas']
    for test in testcases:
        return_str = longestPalindrome(test)
        print("{}".format(return_str))

import cProfile
cProfile.run('main()')

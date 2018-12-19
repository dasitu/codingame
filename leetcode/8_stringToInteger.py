def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    import re
    import math
    number_and_hyphen = re.search(r'^(-|\+)?\d+', str.lstrip())
    if number_and_hyphen is not None:
        return_num = int(number_and_hyphen[0])
        max_num = int(math.pow(2,31) - 1)
        min_num = int(-1 * math.pow(2,31))
        if return_num > max_num:
            return max_num
        elif return_num < min_num:
            return min_num
        return return_num
    return 0

def main():
    testcases = ["-+1", "+1", "0-1", "-", "", "42", "   -42", "4193 with words", "words and 987", "-91283472332"]
    for s in testcases:
        return_str = myAtoi(s)
        print("{}: {}".format(s, return_str))

main()
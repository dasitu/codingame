def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    exchange = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    special = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    total = 0
    s_len = len(s)
    index = 0
    while index < s_len:
        char = s[index]
        next_index = index + 1
        if next_index < s_len:
            next_key = char + s[next_index]
            if next_key in special.keys():
                total += special[next_key]
                index += 2
                continue
        index += 1
        total += exchange[char]
    return total


testcase = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
for test in testcase:
    print(romanToInt(test))


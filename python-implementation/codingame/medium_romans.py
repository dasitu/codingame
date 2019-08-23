import sys


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


def intToRoman(num):
    """
    :type s: int
    :rtype: str
    """
    exchange = {
        1: 'I',
        10: 'X',
        100: 'C',
        1000: 'M',
        4: 'IV',
        5: 'V',
        9: 'IX',
        40: 'XL',
        50: 'L',
        90: 'XC',
        400: 'CD',
        500: 'D',
        900: 'CM',
        4000: 'MMMM'
    }

    roman = ''
    str_num = str(num)
    len_num = len(str_num)
    for index, digital in enumerate(str_num):
        pos_value = 10 ** (len_num - index - 1)
        digital_int = int(digital)
        if digital_int not in exchange.keys():
            if digital_int > 5:
                digital_int = digital_int - 5
                roman += exchange[5 * pos_value]
            roman += exchange[pos_value] * digital_int
        else:
            roman += exchange[pos_value * digital_int]
    return roman


rom_1 = romanToInt(input())
rom_2 = romanToInt(input())
print("{}+{}".format(rom_1, rom_2), file=sys.stderr)
print(intToRoman(rom_1 + rom_2))

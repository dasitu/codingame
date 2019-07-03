def intToRoman(num):
    """
    :type s: str
    :rtype: int
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
        900: 'CM'
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
                roman += exchange[5*pos_value]
            roman += exchange[pos_value] * digital_int
        else:
            roman += exchange[pos_value*digital_int]
    return roman

testcases = [3,4,9,58,1994]
for test in testcases:
    print(intToRoman(test))
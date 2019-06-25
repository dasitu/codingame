def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s

    # initial empty index_matrix
    index_matrix = {}
    for i in range(1, numRows+1):
        index_matrix[i] = ""

    row_direct = 1
    row_index = 1
    for char in s:
        # assign the value directly
        index_matrix[row_index] += char
        # change the index for next use
        row_index += row_direct
        # change the direction for next use
        if row_index == 1 or row_index == numRows:
            row_direct = -1 * row_direct

    # output the needed string by row
    output = ""
    for i in range(1, numRows+1):
        output += index_matrix[i]

    return output

def main():
    testcases = [('AB',1), ('PAYPALISHIRING',3), ('PAYPALISHIRING',4)]
    for s, n in testcases:
        return_str = convert(s,n)
        print("{}".format(return_str))

import cProfile
cProfile.run('main()')
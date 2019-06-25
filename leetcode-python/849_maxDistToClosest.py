def maxDistToClosest(seats):

    # Solution 1, clear and short
    # seats = ''.join(str(e) for e in seats)
    # zero_seats_list = seats.split('1')
    # max_zero_len = max(len(elem) for elem in zero_seats_list)
    # max_distance = (max_zero_len + 1)//2
    # return max(max_distance, len(zero_seats_list[0]), len(zero_seats_list[-1]))

    # minimize the loop times, but looks like the time consuming is similar
    max_zero_between = 0
    leading_one_found = False
    leading_zero = 0
    zero_between = 0

    index = 0
    while index < len(seats):
        if seats[index] == 0:
            if leading_one_found:
                zero_between += 1
            else:
                leading_zero += 1
        else:
            leading_one_found = True
            max_zero_between = max(zero_between, max_zero_between)
            zero_between = 0
        index += 1

    return max((max_zero_between+1)//2, leading_zero, zero_between)

a = [
    [0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1],
    [0,1,1,1,0,0,1,0,0],
    [1,0,0,1],
    [1,0,0,0,1,0,1],
    [1,0,0,1,0,0,1],
    [1,0,0,0],
    [0,0,0,1],
    [0,0,1,1,0],
    [1,0,1,0,1]
]

for s in a:
    print(maxDistToClosest(s))
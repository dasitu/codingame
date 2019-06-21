import sys


def create_tuple_list(row_num, col_num, row_starter=0, col_starter=0):
    tuple_list = []
    for i in range(row_num):
        tuple_list.extend([(i + row_starter, j + col_starter) for j in range(col_num)])
    return tuple_list

n = int(input())
l = int(input())
dark_spots = create_tuple_list(n, n)

for row in range(n):
    line_spots = input().split()
    for col in range(n):
        if line_spots[col] == 'C':
            light_spots = create_tuple_list(2*l-1, 2*l-1, row-(l-1), col-(l-1))
            for spot in light_spots:
                if spot in dark_spots:
                    dark_spots.remove(spot)

print(len(dark_spots))

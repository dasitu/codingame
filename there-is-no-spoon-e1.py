import sys
import math
import numpy

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

print("width:{},height:{}".format(width,height), file=sys.stderr)

cell_matrix = []

i = j = 0
for i in range(height):
    line = list(input())  # width characters, each either 0 or .
    #print("line:{}".format(line), file=sys.stderr)
    cell_matrix.append(line)

print("cell_matrix:{}".format(cell_matrix), file=sys.stderr)

# Three coordinates: a node, its right neighbor, its bottom neighbor
for col in range(width):
    for row in range(height):
        output = ''
        print("row:{},col:{}".format(row,col), file=sys.stderr)
        if cell_matrix[row][col] == '0':
            output = '{} {} '.format(col, row)

            # right cell
            for i in range(width-col):
                right_col = i + col + 1
                print("right_col:{}".format(right_col), file=sys.stderr)
                if right_col < width and cell_matrix[row][right_col] == '0':
                    print("matched", file=sys.stderr)
                    output += '{} {} '.format(right_col,row)
                    break
                if right_col >= width - 1:
                    output += '{} {} '.format('-1','-1')
                    break

            # down cell
            for i in range(height-row):
                down_row = i + row + 1
                print("down_row:{}".format(down_row), file=sys.stderr)
                if down_row < height and cell_matrix[down_row][col] == '0':
                    print("matched", file=sys.stderr)
                    output += '{} {} '.format(col,down_row)
                    break
                if down_row >= height - 1:
                    output += '{} {} '.format('-1','-1')
                    break
        print("output:{}".format(output), file=sys.stderr)
        print("=====", file=sys.stderr)
        if len(output) >= 12:
            print(output)
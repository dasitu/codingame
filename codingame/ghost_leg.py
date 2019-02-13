import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

game_matrix = []
#w, h = [int(i) for i in input().split()]

w = 7
h = 7
input_text = ["A  B  C",
              "|  |  |",
              "|--|  |",
              "|  |--|",
              "|  |--|",
              "|  |  |",
              "1  2  3"]

for i in range(h):
    # line = list(input())
    line = list(input_text[i])
    game_matrix.append(line)


print("map:{}".format(game_matrix), file=sys.stderr)

col_index = 0
for col_index, label in enumerate(game_matrix[0]):
    if label != " ":
        row_index = 0
        current_char = ""
        while row_index < h:
            print("row:{},col:{}".format(row_index,col_index), file=sys.stderr)
            current_char = game_matrix[row_index][col_index]
            left_col = col_index - 1
            right_col = col_index + 1
            left_char = ""
            right_char = ""
            if left_col in range(w):
                left_char = game_matrix[row_index][left_col]
            if right_col in range(w):
                right_char = game_matrix[row_index][right_col]

            if left_char == '-':
                col_index -= 3
            elif right_char == '-':
                col_index += 3
            row_index += 1
        print("{}{}".format(label, current_char))

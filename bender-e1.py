import sys
import numpy as np


class Bender:
    cur_l = 0
    cur_c = 0
    cur_d = 'S'
    is_bear = False
    is_invert = False
    direct_priority = 'SENW'
    foot_print = []
    moves = []

    def __init__(self, start_row=0, start_col=0):
        self.cur_l = start_row
        self.cur_c = start_col

    def change_bear_mode(self):
        self.is_bear = not self.is_bear

    def change_invert_mode(self):
        self.is_invert = not self.is_invert
        self.direct_priority = self.direct_priority[::-1]

    def set_direction(self, new_direct):
        self.cur_d = new_direct

    def reset_foot_print(self):
        self.foot_print.clear()

    def move_in_state_by_content(self, content):
        if content == '#':
            return 'blocked'
        if content == 'X' and not self.is_bear:
            return 'blocked'
        if content == 'X' and self.is_bear:
            return 'destroyed'
        return 'passed'

    def move_to_pos(self, row, col, content):
        current_state = [self.cur_l, self.cur_c, self.cur_d, self.is_bear, self.is_invert, content]
        self.foot_print.append(current_state)
        self.moves.append(self.cur_d)
        self.cur_l = row
        self.cur_c = col

    def jump_to_pos(self, row, col):
        self.cur_l = row
        self.cur_c = col

    def check_is_loop(self, content):
        current_state = [self.cur_l, self.cur_c, self.cur_d, self.is_bear, self.is_invert, content]
        for history in self.foot_print:
            if history == current_state:
                return True
        return False


class CityMap:
    map_array = np.array([])

    def __init__(self, init_map=None):
        if init_map is None:
            init_map = []
        self.map_array = np.array(init_map)

    def get_content(self, row, col):
        content = self.map_array[row][col]
        return content

    def set_content(self, row, col, content):
        row_str = self.map_array[row]
        row_str[col] = content
        self.map_array[row] = row_str

    def get_trans_pos(self, row, col):
        trans_pos = self.get_pos_of_symbol('T')
        if len(trans_pos) != 2:
            print_debug('Impossible')
        elif (row, col) in trans_pos:
            trans_pos.remove((row, col))
        return trans_pos[0]

    def get_start_pos(self):
        (row, col) = self.get_pos_of_symbol('@')[0]
        return int(row), int(col)

    def get_pos_of_symbol(self, symbol):
        pos = []
        row = 0
        for row_str in self.map_array:
            if symbol in row_str:
                col = list(row_str).index(symbol)
                pos.append((row, col))
            row += 1
        return pos

    def print_map(self):
        row_num, col_num = self.map_array.shape
        width = max(len(str(row_num)), len(str(col_num)))
        col_label = ' ' + ''.join('{0:{1}}'.format(x, width) for x in range(col_num))
        row_label = list(range(row_num))
        print_debug(col_label)
        for row_label, row in zip(row_label, self.map_array):
            print_debug('{0:{2}}{1:}'.format(row_label, ''.join('{0:{1}}'.format(i, width) for i in row), width))


def print_debug(msg):
    print(msg, file=sys.stderr)


def get_input():
    input_map = []
    l, c = [int(i) for i in input().split()]
    for i in range(l):
        row = list(input())
        input_map.append(row)
    print_debug(input_map)
    return input_map


def format_output(moves):
    mapping = {'S': 'SOUTH', 'E': 'EAST', 'N': 'NORTH', 'W': 'WEST'}
    output = ''
    for seq_str in moves:
        output += mapping[seq_str]+'\n'
    return output


def get_pos_by_direct(cur_row, cur_col, cur_dir):
    new_row = cur_row
    new_col = cur_col
    if cur_dir == 'S':
        new_row = cur_row + 1
    elif cur_dir == 'E':
        new_col = cur_col + 1
    elif cur_dir == 'N':
        new_row = cur_row - 1
    elif cur_dir == 'W':
        new_col = cur_col - 1
    return new_row, new_col


whole_map = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', ' ', ' ', '#', '@', '#', 'I', ' ', ' ', 'T', '$', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', 'I', 'B', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', 'W', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', 'B', ' ', 'X', 'B', 'N', '#', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', 'W', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', 'B', ' ', 'X', 'B', 'N', '#', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', 'W', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', 'B', ' ', 'X', 'B', 'N', '#', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', 'X', 'B', 'I', 'T', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'], ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#'], ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

whole_map = np.array(whole_map)
#whole_map = []
if len(whole_map) == 0:
    whole_map = get_input()

city_map = CityMap(whole_map)
city_map.print_map()

bender = Bender(*city_map.get_start_pos())
is_loop = False

while 1:
    cur_content = city_map.get_content(bender.cur_l, bender.cur_c)

    if cur_content in 'SENW':
        bender.set_direction(cur_content)
    if cur_content == 'I':
        bender.change_invert_mode()
    if cur_content == 'B':
        bender.change_bear_mode()
    if cur_content == 'T':
        new_l, new_c = city_map.get_trans_pos(bender.cur_l, bender.cur_c)
        bender.jump_to_pos(new_l, new_c)

    print_debug(bender.foot_print[-1:])
    if cur_content == '$':
        break
    is_loop = bender.check_is_loop(cur_content)
    if is_loop:
        break

    # try next pos without change direction
    next_l, next_c = get_pos_by_direct(bender.cur_l, bender.cur_c, bender.cur_d)
    next_content = city_map.get_content(next_l, next_c)
    move_in_state = bender.move_in_state_by_content(next_content)
    if move_in_state == 'passed':
        bender.move_to_pos(next_l, next_c, cur_content)
    elif move_in_state == 'destroyed':
        city_map.set_content(next_l, next_c, ' ')
        bender.move_to_pos(next_l, next_c, cur_content)
        bender.reset_foot_print()
    elif move_in_state == 'blocked':
        # try to change direction according to the bender direction priority
        direct_priority = bender.direct_priority
        is_loop = True
        for direct in direct_priority:
            next_l, next_c = get_pos_by_direct(bender.cur_l, bender.cur_c, direct)
            next_content = city_map.get_content(next_l, next_c)
            move_in_state = bender.move_in_state_by_content(next_content)
            if move_in_state == 'blocked':
                continue
            elif move_in_state == 'passed':
                bender.set_direction(direct)
                bender.move_to_pos(next_l, next_c, cur_content)
                is_loop = False
                break
            elif move_in_state == 'destroyed':
                city_map.set_content(next_l, next_c, ' ')
                bender.set_direction(direct)
                bender.move_to_pos(next_l, next_c, cur_content)
                bender.reset_foot_print()
                is_loop = False
                break

if not is_loop:
    print(format_output(bender.moves))
else:
    print('LOOP')

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def print_debug(msg):
    print(msg, file=sys.stderr)

def add_elevator(floor, pos, elevators):
    if floor not in elevators.keys():
        elevators[floor] = [pos]
    else:
        elevators[floor].append(pos)

def select_best_floor_to_build_elevator(exit_floor, clone_floor, clone_pos, elevators, nb_additional_elevators, direction):
    floors = list(range(clone_floor, exit_floor))
    floor_length_to_elevator_mapping = {}
    for floor in floors:
        elevators_pos = elevators[floor]
        nearest_elev_pos = select_nearest_elev(clone_pos, elevators_pos, direction)
        floor_length_to_elevator_mapping[floor] = abs(nearest_elev_pos - clone_pos)

    # sorted floors by length to nearest_elev_pos
    sorted_floors = [k for k in sorted(floor_length_to_elevator_mapping, key=floor_length_to_elevator_mapping.get, reverse=True)]

    return sorted_floors[0:nb_additional_elevators]

def is_every_floor_has_elevator(exit_floor, clone_floor, elevators):
    floors = list(range(clone_floor, exit_floor))
    elevator_count = 0
    for floor in floors:
        if floor in elevators.keys():
            elevator_count += 1
    if len(floors) == elevator_count:
        return True
    return False

def floors_to_build_elev(exit_floor, clone_floor, clone_pos, elevators, nb_additional_elevators, direction):
    floors_to_build = []
    if clone_floor != exit_floor:
        # build elevator if this floor does not have
        if clone_floor not in elevators.keys():
            print_debug('build on current floor')
            if nb_additional_elevators != 0:
                return [clone_floor]
        # we can build additional elevator to optimize the path
        if is_every_floor_has_elevator(exit_floor, clone_floor, elevators):
            print_debug('+++++All have elev++++')
            floors_to_build = select_best_floor_to_build_elevator(exit_floor, clone_floor, clone_pos, elevators, nb_additional_elevators, direction)
    return floors_to_build

def is_wait_state(clone_floor, clone_pos, direction):
    if clone_floor == -1 or clone_pos == -1 or direction == 'NONE':
        return True
    return False

def get_direct_to_target(current_pos, target_pos):
    direct = ''
    if current_pos > target_pos:
        direct = 'LEFT'
    elif current_pos < target_pos:
        direct = 'RIGHT'
    elif current_pos == target_pos:
        direct = 'HIT'
    return direct

def select_nearest_elev(current_pos, elevators_pos, current_direct):
    target_elevator_pos = ''
    min_diff = 99
    for elevator_pos in elevators_pos:
        #print_debug('working on elev:{}'.format(elevator_pos))
        pos_diff = abs(elevator_pos - current_pos)
        pos_direct = get_direct_to_target(current_pos, elevator_pos)
        #print_debug('pos_diff:{}'.format(pos_diff))
        #print_debug('min_diff:{}'.format(min_diff))
        #print_debug('pos_direct:{}'.format(pos_direct))
        if pos_diff < min_diff:
            min_diff = pos_diff
            target_elevator_pos = elevator_pos
        elif pos_diff == min_diff:
            if current_direct == pos_direct:
                min_diff = pos_diff
                target_elevator_pos = elevator_pos
    #print_debug('best elev:{}'.format(target_elevator_pos))
    return target_elevator_pos

def get_direct_to_exit(clone_pos, clone_floor, exit_pos, exit_floor):
    right_direct_to_exit = ''
    if clone_floor == exit_floor:
        right_direct_to_exit = get_direct_to_target(clone_pos, exit_pos)
    return right_direct_to_exit

def get_direct_to_elevator(clone_pos, clone_floor, elevators, direction):
    right_direct_to_elevator = ''
    if clone_floor in elevators.keys():
        elevators_pos = elevators[clone_floor]
        nearest_elev_pos = select_nearest_elev(clone_pos, elevators_pos, direction)
        right_direct_to_elevator = get_direct_to_target(clone_pos, nearest_elev_pos)
    return right_direct_to_elevator

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators
# nb_elevators: number of elevators
elevators = {}
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    add_elevator(elevator_floor, elevator_pos, elevators)

print_debug('nb_floors:{}'.format(nb_floors))
print_debug('width:{}'.format(width))
print_debug('nb_rounds:{}'.format(nb_rounds))

print_debug('nb_total_clones:{}'.format(nb_total_clones))
print_debug('nb_additional_elevators:{}'.format(nb_additional_elevators))
print_debug('nb_elevators:{}'.format(nb_elevators))
print_debug('elevators:{}'.format(elevators))
print_debug('=========loop=======')

# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    wait_state = is_wait_state(clone_floor, clone_pos, direction)
    if wait_state:
        print("WAIT")
        continue

    floors_to_build = floors_to_build_elev(exit_floor, clone_floor, clone_pos, elevators, nb_additional_elevators, direction)
    direct_to_exit = get_direct_to_exit(clone_pos, clone_floor, exit_pos, exit_floor)
    direct_to_elevator = get_direct_to_elevator(clone_pos, clone_floor, elevators, direction)
    right_direct = direct_to_exit if direct_to_exit != '' else direct_to_elevator

    print_debug('clone_floor:{}'.format(clone_floor))
    print_debug('clone_pos:{}'.format(clone_pos))
    print_debug('exit_floor:{}'.format(exit_floor))
    print_debug('exit_pos:{}'.format(exit_pos))
    print_debug('elevators:{}'.format(elevators))
    print_debug('nb_additional_elevators:{}'.format(nb_additional_elevators))
    print_debug('floors_to_build:{}'.format(floors_to_build))
    print_debug('direction:{}'.format(direction))
    print_debug('right_direct:{}'.format(right_direct))

    if clone_floor in floors_to_build:
        print('ELEVATOR')
        nb_additional_elevators -= 1
        add_elevator(clone_floor, clone_pos, elevators)
        continue

    if direction != right_direct and right_direct != 'HIT':
        print('BLOCK')
        continue

    print('WAIT')
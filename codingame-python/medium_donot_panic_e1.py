import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def print_debug(msg):
    print(msg, file=sys.stderr)

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
elevators = {}
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

print_debug('nb_floors:{}'.format(nb_floors))
print_debug('width:{}'.format(width))
print_debug('nb_rounds:{}'.format(nb_rounds))
print_debug('exit_floor:{}'.format(exit_floor))
print_debug('exit_pos:{}'.format(exit_pos))
print_debug('nb_total_clones:{}'.format(nb_total_clones))
print_debug('nb_additional_elevators:{}'.format(nb_additional_elevators))
print_debug('nb_elevators:{}'.format(nb_elevators))
print_debug('elevators:{}'.format(elevators))

# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    print_debug('clone_floor:{}'.format(clone_floor))
    print_debug('clone_pos:{}'.format(clone_pos))
    print_debug('direction:{}'.format(direction))

    right_direct = ''
    if clone_pos > exit_pos:
        right_direct = 'LEFT'
    elif clone_pos < exit_pos:
        right_direct = 'RIGHT'

    if clone_floor in elevators.keys():
        right_direct_to_elevator = ''
        if clone_pos > elevators[clone_floor]:
            right_direct_to_elevator = 'LEFT'
        elif clone_pos < elevators[clone_floor]:
            right_direct_to_elevator = 'RIGHT'

    if clone_floor == exit_floor and clone_floor != -1:
        print_debug('=====1=======')
        print_debug('right_direct:{}'.format(right_direct))
        if direction != right_direct:
            print('BLOCK')
            continue
    elif clone_floor != -1 and right_direct_to_elevator:
        print_debug('=====2====')
        print_debug('right_direct_to_elevator:{}'.format(right_direct_to_elevator))
        if direction != right_direct_to_elevator:
            print('BLOCK')
            continue

    # action: WAIT or BLOCK
    print("WAIT")
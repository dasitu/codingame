import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

g = -3.711

def print_debug(msg):
    print(msg, file=sys.stderr)

def cal_dist_to_target(position, target):
    print_debug('target:{}'.format(target))
    x_diff = abs(target[0] - position[0])
    y_diff = abs(target[1] - position[1])
    dist = math.sqrt(math.pow(x_diff,2) + math.pow(y_diff,2))
    return dist

def cal_next_state(current_state, time_in_sec=1):
    x, y, h_speed, v_speed, fuel, rotate, power = current_state

    a_x = power*math.sin((math.radians(rotate*-1)))
    a_y = power*math.cos((math.radians(abs(rotate)))) + g
    print_debug("a_x:{},a_y:{}".format(a_x,a_y))

    speed_x = h_speed + a_x * time_in_sec
    speed_y = v_speed + a_y * time_in_sec
    print_debug("speed_x:{},speed_y:{}".format(speed_x, speed_y))

    next_x = x + (h_speed + speed_x) * 0.5 * time_in_sec
    next_y = y + (v_speed + speed_y) * 0.5 * time_in_sec

    next_fuel = fuel - (power * time_in_sec)
    next_state = [next_x, next_y, speed_x, speed_y, next_fuel]

    return next_state


surface_n = int(input())  # the number of points used to draw the surface of Mars.

last_x = 0
last_y = 0
landing_x = []
landing_y = 0

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    #print("land_x:{},land_y:{}".format(land_x,land_y), file=sys.stderr)
    if land_y == last_y:
        landing_x = [last_x,land_x]
        landing_y = land_y
    else:
        last_x = land_x
        last_y = land_y
print("landing place {}".format(landing_x), file=sys.stderr)

landing_length = landing_x[1] - landing_x[0]
target_landing = [landing_x[1], landing_y]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = current_state = [int(i) for i in input().split()]

    # for all possible 9 choices for power and rotate
    # calculate which one have the shortest distance to the target

    rotate_range = [-15, 0, 15]
    power_range = [-1, 0, 1]
    new_rotate = selected_rotate = 0
    new_power = selected_power = 0
    smallest_dist = 9999

    for rotate_chg in rotate_range:
        new_rotate = rotate + rotate_chg
        if new_rotate < -90:
            new_rotate = -90
        if new_rotate > 90:
            new_rotate = 90
        for power_chg in power_range:
            new_power = power + power_chg
            if new_power < 0:
                new_power = 0
            if new_power > 4:
                new_power = 4
            current_state[5] = new_rotate
            current_state[6] = new_power
            print("new {},{}".format(new_rotate, new_power), file=sys.stderr)
            print("new state:{}".format(current_state), file=sys.stderr)
            next_x, next_y, speed_x, speed_y, next_fuel = cal_next_state(current_state)
            next_pos = [next_x, next_y]
            print("next pos:{}".format(next_pos), file=sys.stderr)
            dist_to_target = cal_dist_to_target(next_pos, target_landing)
            print("dist_to_target:{}".format(dist_to_target), file=sys.stderr)
            print("smallest_dist:{}".format(smallest_dist), file=sys.stderr)
            if dist_to_target < smallest_dist:
                selected_rotate = new_rotate
                selected_power = new_power
                smallest_dist = dist_to_target

        # limit the speed
        if v_speed > 40 or h_speed > 20 and power > 1:
            selected_power -= 1

    # make sure landing rotate is 0
    if y < landing_y - (((abs(rotate)/15) + 1) * v_speed):
        selected_rotate = 0

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print("{} {}".format(selected_rotate, selected_power))
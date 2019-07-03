import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def normal_round(n, strategy='down'):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    
    if n - math.floor(n) > 0.5:
        return math.ceil(n)
    
    if n - math.floor(n) == 0.5:
        if strategy == 'down':
            return math.floor(n)
        else:
            return math.ceil(n)
    
def round_to_rg_str(round_count):
    rg_str = round_count.__str__() + ':'
    for i in range(round_count):
        if ((i+1) % 2) == 0: #i started from 0, so add 1 to make it started from 1. keep it the same as light_round.
            rg_str += 'R'
        else:
            rg_str += 'G'
    return rg_str

max_speed = int(input())
light_count = int(input())
lights = []
last_consumed_second = 0
last_min_speed = max_speed
total_sec = 0
total_dis = 0
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    print("distance:{}, duration:{}".format(distance,duration), file=sys.stderr)
    total_dis += distance
    
    mod_sec = total_sec % duration
    light_round = int(total_sec // duration) 
    print("passed light round:{}".format(light_round), file=sys.stderr)
    
    current_round = 1
    min_speed = round((distance/1000)/((duration*current_round)/3600),2)
    print("first round:{}, min_speed:{}".format(round_to_rg_str(current_round), min_speed), file=sys.stderr)
    
    while normal_round(min_speed) > normal_round(last_min_speed):
        current_round += 1
        min_speed = round((distance/1000)/((duration*current_round)/3600),2)
        print("try rounds:{}, min_speed:{}".format(round_to_rg_str(current_round), min_speed), file=sys.stderr)
    
    light_round += current_round
    print("total light round:{}".format(light_round), file=sys.stderr)
    # there is duration left and current light is red
    #if mod_sec != 0 and (light_round % 2) != 0:
    #    current_round += 1;
    #    light_round += 1
    #    min_speed = round((distance/1000)/((duration*current_round)/3600),2)
    #    print("left round:{}, min_speed:{}".format(round_to_rg_str(light_round), min_speed), file=sys.stderr)
        
    # you can use the max speed for the first round to pass the green light
    if min_speed < max_speed and light_round == 1:
        min_speed = max_speed
    
    if min_speed < last_min_speed:
        last_min_speed = min_speed
    total_sec = normal_round((total_dis/1000)/last_min_speed*3600)
    print("last_min_speed:{}".format(last_min_speed), file=sys.stderr)
    print("total_sec:{}".format(total_sec), file=sys.stderr)
    lights.append([distance,duration,light_round,min_speed])
    print("======", file=sys.stderr)

lights_matrix = np.array(lights)
row_count = np.size(lights_matrix,0)
col_count = np.size(lights_matrix,1)

print("max speed:{}, light_count:{}".format(max_speed,light_count), file=sys.stderr)
#print("lights_matrix:{}x{}".format(row_count,col_count), file=sys.stderr)
#print("lights:{}".format(lights), file=sys.stderr)

speed = normal_round(min(lights_matrix[:,col_count-1]))

print(speed)
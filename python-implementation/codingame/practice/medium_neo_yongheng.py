import sys
import math
from fractions import Fraction
from decimal import Decimal

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
low_threshold = 1


class Interval(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __repr__(self):
        return repr((self.start, self.end))

class Light(object):
    def __init__(self, distance, duration):
        self.distance = Decimal(distance) * Decimal('3.6')
        self.duration = Decimal(duration)

    def green_speed_intervals(self, max_speed, min_speed):
        speed_interval = []
        is_green = False
        for i in range(1, 9999):
            is_green = (is_green == False)

            if not is_green:
                continue

            lower_time = (i-1) * self.duration
            upper_time = i* self.duration
            if (lower_time == 0):
                upper_speed = max_speed
            else:
                upper_speed = self.distance/lower_time

            lower_speed = self.distance/upper_time
            if (lower_speed > upper_speed or lower_speed > max_speed ):
                continue
            if (upper_speed < min_speed):
                break

            interval = Interval(lower_speed, upper_speed)
            speed_interval.append(interval)
        print(speed_interval, file=sys.stderr)
        return speed_interval

    def __repr__(self):
        return repr((self.distance, self.duration))

class Road(object):
    def __init__(self, lights, max_speed, min_speed):
        self.lights = lights
        self.max_s = max_speed
        self.min_s = min_speed
        self.green_intervals = []

    def calc_all_green_intervals(self):
        for light in self.lights:
            self.green_intervals.append(light.green_speed_intervals(self.max_s, self.min_s))

    def calc_cross_intervals(self):
        if(len(self.green_intervals) == 1):
            return self.green_intervals[0]
        else:
            base_speed = self.green_intervals[0]
            for i in range(1, len(self.green_intervals) - 1):
                temp_speed = []
                for speed_interval in self.green_intervals[i]:
                    for base_interval in base_speed:
                        if (speed_interval.start <= base_interval.end and speed_interval.end >= base_interval.start):
                            temp_interval = Interval(base_interval.start, base_interval.end)
                            if (base_interval.start <= speed_interval.start):
                                temp_interval.start = speed_interval.start
                            if (base_interval.end >= speed_interval.end):
                                temp_interval.end = speed_interval.end
                            temp_speed.append(temp_interval)
                        elif (speed_interval.start > base_interval.end):
                            break

                base_speed = temp_speed
            print(base_speed, file=sys.stderr)
            return base_speed

    def find_max_speed(self):
        if(len(self.green_intervals) == 0):
            self.calc_all_green_intervals()
        intervals = self.calc_cross_intervals()
        if(intervals is None or len(intervals) == 0):
            return None
        else:
            for i in range(0, len(intervals)):
                # only 1 value in the section. just ignore
                if (intervals[i].start == intervals[i].end):
                    continue
                upper = int(intervals[i].end )
                lower = int(intervals[i].start)

                print(upper, file=sys.stderr)

                if (int(upper) > int(lower)):
                    return int(upper)

    def __repr__(self):
        return repr((self.max_s, self.min_s, self.lights))

speed = int(input())
print(speed, file=sys.stderr)
light_count = int(input())

all_lights = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    light = Light(distance, duration)
    print(light, file=sys.stderr)
    all_lights.append(light)

road = Road(all_lights, speed, 1)
print(road, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(road.find_max_speed())

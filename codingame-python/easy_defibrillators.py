# https://www.codingame.com/ide/puzzle/defibrillators
import sys
import math


def distance(pos_a: tuple, pos_b: tuple) -> float:
    # pos is tuple (lon, lat) in degrees
    lon_a = math.radians(pos_a[0])
    lat_a = math.radians(pos_a[1])
    lon_b = math.radians(pos_b[0])
    lat_b = math.radians(pos_b[1])
    x = (lon_b - lon_a) * math.cos((lat_a + lat_b)/2)
    y = lat_b - lat_a
    d = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) * 6371
    return d


lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())
user_pos = (lon, lat)

closest_d = 6371
closest_name = ""
for i in range(n):
    defib = input().split(';')
    d = distance(user_pos, (float(defib[4].replace(',', '.')), float(defib[5].replace(',', '.'))))
    if d < closest_d:
        closest_d = d
        closest_name = defib[1]

print(closest_name)
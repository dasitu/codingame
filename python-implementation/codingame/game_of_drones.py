# https://www.codingame.com/ide/puzzle/game-of-drones

import sys
import math


class Identity:
    id = 0
    x = 0
    y = 0
    owner_id = 0

    def __str__(self):
        return "id:{},({},{}),owner:{}".format(self.id, self.x, self.y, self.owner_id)


class Zone(Identity):
    drones = []

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


class Drone(Identity):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Player:
    id = 0
    drones = []

    def __init__(self, id):
        self.id = id

    def add_drone(self, drone):
        self.drones.append(drone)


def get_distance(x1, y1, x2, y2):
    # The ground flown over by the drones is rectangular,
    # it is 4,000 units in wide and 1,800 units high.
    # The coordinate 0,0 is at the top-left.
    return math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))


def find_nearest_zone(all_zones, x, y):
    empty_x, empty_y, empty_shortest = 0, 0, 4000
    # my_x, my_y, my_shortest = 0, 0, 4000
    other_x, other_y, other_shortest = 0, 0, 4000

    for zone in all_zones:
        dis = get_distance(zone.x, zone.y, x, y)
        print("({},{})->({},{}):{}".format(zone.x,
                                           zone.y, x, y, dis), file=sys.stderr)
        if zone.owner_id == -1:
            if dis < empty_shortest:
                empty_x, empty_y = zone.x, zone.y
                empty_shortest = dis
        else:
            if dis < other_shortest:
                other_x, other_y = zone.x, zone.y
                other_shortest = dis

    if empty_shortest != 4000:
        return empty_x, empty_y

    if other_shortest != 4000:
        return other_x, other_y


# player_count: number of players in the game (2 to 4 players)
# my_id: ID of your player (0, 1, 2, or 3)
# drone_count: number of drones in each team (3 to 11)
# zone_count: number of all_zones on the map (4 to 8)
player_count, my_id, drone_count, zone_count = [
    int(i) for i in input().split()]

print("my_id:", my_id, file=sys.stderr)
all_zones = []
for i in range(zone_count):
    # x: corresponds to the position of the center of a zone. A zone is a circle with a radius of 100 units.
    x, y = [int(j) for j in input().split()]
    zone = Zone(i, x, y)
    all_zones.append(zone)
    print(zone, file=sys.stderr)

# game loop
while True:
    all_players = []
    for i in range(zone_count):
        # ID of the team controlling the zone (0, 1, 2, or 3) or -1 if it is not controlled.
        # The all_zones are given in the same order as in the initialization.
        all_zones[i].owner_id = int(input())

    for i in range(player_count):
        single_player = []
        for j in range(drone_count):
            # dx: The first D lines contain the coordinates of drones of a player with the ID 0,
            # the following D lines those of the drones of player 1, and thus it continues until the last player.
            dx, dy = [int(k) for k in input().split()]
            single_player.append((dx, dy))
            print("{}:{}".format(i, single_player), file=sys.stderr)
        all_players.append(single_player)

    for i in range(drone_count):
        sx, sy = find_nearest_zone(
            all_zones, all_players[my_id][i][0], all_players[my_id][i][1])
        print("output:{},{}".format(sx, sy), file=sys.stderr)
        print("{} {}".format(sx, sy))

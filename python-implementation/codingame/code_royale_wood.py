import sys
import math


class Site(object):
    def __init__(self, site_id, x, y, radius):
        self.site_id = site_id
        self.x = x
        self.y = y
        self.radius = radius
        self.gold_remain = -1
        self.max_mine_rate = -1
        self.structure_type = -1
        self.owner = -1
        self.param_1 = -1
        self.param_2 = -1

    def __str__(self):
        return "site-{}:({},{})|R:{}|T:{}|O:{}|P1:{}|P2:{}".format(self.site_id, self.x, self.y, self.radius,
                                                                   self.structure_type, self.owner, self.param_1,
                                                                   self.param_2)


class Unit:
    def __init__(self, x, y, owner, unit_type, health):
        self.x = x
        self.y = y
        self.owner = owner
        self.unit_type = unit_type
        self.health = health

    def __str__(self):
        return "unit:({},{})|my:{}|t:{}|H:{}".format(self.x, self.y, self.owner, self.unit_type, self.owner)


def get_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def get_nearest_corner_to_queen(queen):
    x_max = 1920
    y_max = 1000
    corner_x = 0 if queen.x < abs(x_max - queen.x) else x_max
    corner_y = 0 if queen.y < abs(y_max - queen.y) else y_max
    print("corner:({},{})".format(corner_x, corner_y), file=sys.stderr)
    return corner_x, corner_y


def find_site_id_build_mine(my_queen, empty_sites):
    available_sites = empty_sites[::]
    for cid in empty_site:
        current_site = sites[cid]
        if current_site.gold_remain == 0:
            available_sites.remove(cid)
    target_x = my_queen.x
    target_y = my_queen.y
    return find_nearest_site_id(target_x, target_y, available_sites)


def find_upgradable_mine_sites(mine_sites):
    available_sites = mine_sites[::]
    for cid in mine_sites:
        current_site = sites[cid]
        if current_site.gold_remain == 0 or current_site.param_1 == current_site.max_mine_rate:
            available_sites.remove(cid)
    return available_sites


def find_site_id_upgrade_mine(my_queen, mine_sites):
    return find_nearest_site_id(my_queen.x, my_queen.y, find_upgradable_mine_sites(mine_sites))


def find_site_id_build_tower(my_queen, empty_sites):
    corner_x, corner_y = get_nearest_corner_to_queen(my_queen)
    target_x = 1920 // 4
    if corner_x == 1920:
        target_x *= 3
    target_y = 1000 // 2
    return find_nearest_site_id(target_x, target_y, empty_sites)


def find_site_id_upgrade_tower():
    return -1


def find_nearest_site_id(target_x, target_y, candidate_id_list):
    nearest_site = -1
    nearest_distance = MAX_DISTANCE
    for cid in candidate_id_list:
        current_site = sites[cid]
        distance = get_distance(target_x, target_y, current_site.x, current_site.y)
        print("target:{},{}".format(target_x,target_y), file=sys.stderr)
        print("({},{}):{}".format(current_site.x, current_site.y, distance), file=sys.stderr)
        if distance < nearest_distance:
            print("nearest_distance:", nearest_distance, file=sys.stderr)
            nearest_site = cid
            nearest_distance = distance
    return nearest_site


def find_training_site(training_sites_id, enemy_q):
    shortest_site_id = find_nearest_site_id(enemy_q.x, enemy_q.y, training_sites_id)
    return shortest_site_id


def tower_covered_range(my_tower_sites):
    x_left = x_right = 1920 // 2
    y_top = y_bottom = 1000 // 2
    for tower_id in my_tower_sites:
        tower = sites[tower_id]
        tower_range = tower.param_2
        x_left = min(x_left, tower.x - tower_range)
        x_right = max(x_right, tower.x + tower_range)
        y_top = min(y_top, tower.y - tower_range)
        y_bottom = max(y_bottom, tower.y + tower_range)
    return x_left, x_right, y_top, y_bottom


def get_total_mine_rate(mine_sites):
    rate = 0
    for mine_id in mine_sites:
        mine = sites[mine_id]
        rate += mine.param_1
    return rate


MAX_DISTANCE = get_distance(0,0,1920,1000)
sites = {}
num_sites = int(input())
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    sites[site_id] = Site(site_id, x, y, radius)
    # print(sites[site_id], file=sys.stderr)

# game loop
while True:
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    # print("touched_site: ", touched_site, file=sys.stderr)

    archer_site = []
    knight_site = []
    tower_site = []
    mine_site = []
    enemy_archer_site = []
    enemy_knight_site = []
    enemy_tower_site = []
    enemy_mine_site = []
    empty_site = []
    for i in range(num_sites):
        # ignore_1: used in future leagues
        # ignore_2: used in future leagues
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, goal_remain, max_rate, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        sites[site_id].structure_type = structure_type
        sites[site_id].owner = owner
        sites[site_id].gold_remain = goal_remain
        sites[site_id].max_mine_rate = max_rate
        sites[site_id].param_1 = param_1
        sites[site_id].param_2 = param_2
        if structure_type == -1:
            empty_site.append(site_id)
        elif structure_type == 2 and param_2 == 0 and owner == 0:
            knight_site.append(site_id)
        elif structure_type == 2 and param_2 == 0 and owner == 1:
            enemy_knight_site.append(site_id)
        elif structure_type == 2 and param_2 == 1 and owner == 0:
            archer_site.append(site_id)
        elif structure_type == 2 and param_2 == 1 and owner == 1:
            enemy_archer_site.append(site_id)
        elif structure_type == 1 and owner == 0:
            tower_site.append(site_id)
        elif structure_type == 1 and owner == 1:
            enemy_tower_site.append(site_id)
        elif structure_type == 0 and owner == 0:
            mine_site.append(site_id)
        elif structure_type == 0 and owner == 1:
            enemy_mine_site.append(site_id)

    print("knight_site:", knight_site, file=sys.stderr)
    print("archer_site:", archer_site, file=sys.stderr)
    print("tower_site:", tower_site, file=sys.stderr)
    print("mine_site:", mine_site, file=sys.stderr)
    print("enemy_knight_site:", enemy_knight_site, file=sys.stderr)
    print("enemy_archer_site:", enemy_archer_site, file=sys.stderr)
    print("enemy_tower_site:", enemy_tower_site, file=sys.stderr)
    print("enemy_mine_site:", enemy_mine_site, file=sys.stderr)
    print("empty_site:", empty_site, file=sys.stderr)
    my_archer_site_count = len(archer_site)
    my_knight_site_count = len(knight_site)
    my_tower_site_count = len(tower_site)
    my_mine_site_count = len(mine_site)
    upgradable_mine_sites = find_upgradable_mine_sites(mine_site)
    mine_rate = get_total_mine_rate(mine_site)
    enemy_archer_site_count = len(enemy_archer_site)
    enemy_knight_site_count = len(enemy_knight_site)
    enemy_tower_site_count = len(enemy_tower_site)
    enemy_mine_site_count = len(enemy_mine_site)

    num_units = int(input())
    my_queen = ""
    my_archers = []
    my_knights = []
    my_giants = []
    enemy_queen = ""
    enemy_archers = []
    enemy_knights = []
    enemy_giants = []
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        unit = Unit(x, y, owner, unit_type, health)
        if owner == 0:
            if unit_type == -1:
                my_queen = unit
            elif unit_type == 0:
                my_knights.append(unit)
            elif unit_type == 1:
                my_archers.append(unit)
            elif unit_type == 2:
                my_giants.append(unit)
        else:
            if unit_type == -1:
                enemy_queen = unit
            elif unit_type == 0:
                enemy_knights.append(unit)
            elif unit_type == 1:
                enemy_archers.append(unit)
            elif unit_type == 2:
                enemy_giants.append(unit)

    print("my_queen:({},{})|{}".format(my_queen.x, my_queen.y, my_queen.health), file=sys.stderr)
    print("enemy_queen:({},{})|{}".format(enemy_queen.x, enemy_queen.y, enemy_queen.health), file=sys.stderr)
    my_knights_count = len(my_knights)
    my_archers_count = len(my_archers)
    my_giants_count = len(my_giants)
    enemy_archers_count = len(enemy_archers)
    enemy_knights_count = len(enemy_knights)
    enemy_giants_count = len(enemy_giants)
    print("my_knights_count:", my_knights_count, file=sys.stderr)
    print("my_archers_count:", my_archers_count, file=sys.stderr)
    print("my_giants_count:", my_giants_count, file=sys.stderr)
    print("enemy_archers_count:", enemy_archers_count, file=sys.stderr)
    print("enemy_knights_count:", enemy_knights_count, file=sys.stderr)
    print("enemy_giants_count:", enemy_giants_count, file=sys.stderr)
    print("mine_rate:", mine_rate, file=sys.stderr)

    # decide build type
    build_type = "TOWER"
    build_site_id = find_nearest_site_id(my_queen.x, my_queen.y, empty_site)
    if my_knight_site_count == 0:
        build_type = "BARRACKS-KNIGHT"
    elif my_mine_site_count == 0 or mine_rate < 3 or (my_tower_site_count > 4 and mine_rate < 7):
        build_type = "MINE"
        build_site_id = find_site_id_build_mine(my_queen, empty_site)
    elif (my_mine_site_count > 3 or my_tower_site_count > 3) and len(upgradable_mine_sites) > 0:
        build_type = "MINE"
        build_site_id = find_site_id_upgrade_mine(my_queen, upgradable_mine_sites)
    elif my_tower_site_count < my_knight_site_count / 2 and my_archers_count < enemy_knights_count / 2 + 2:
        build_type = "TOWER"
        build_site_id = find_site_id_build_tower(my_queen, empty_site)
    elif my_archers_count == 0 and my_knights_count > 0 and len(archer_site) == 0:
        build_type = "BARRACKS-ARCHER"

    # decide training type
    training_sites_type = knight_site
    if my_archers_count < enemy_knights_count / 2 - my_tower_site_count and len(archer_site) > 0:
        training_sites_type = archer_site
    # where to train, shortest to enemy queen
    training_site_id = find_training_site(training_sites_type, enemy_queen)
    print("training site:", training_site_id, file=sys.stderr)
    train_cmd = "TRAIN"
    if training_site_id != -1:
        train_cmd += " " + str(training_site_id)

    # build or not
    print("BUILD {} {}".format(build_site_id, build_type))
    print(train_cmd)

def gardenNoAdj(N, paths):
    output_garden = []
    garden_map = {}

    for i in range(1, N+1):
        garden_map[i] = []
        output_garden.append(0)
    for path in paths:
        garden_map[path[0]].append(path[1])
        garden_map[path[1]].append(path[0])

    for i in range(1, N+1):
        available_type = [1, 2, 3, 4]
        nebors = garden_map[i]
        for nebor in nebors:
            neb_type = output_garden[nebor-1]
            if neb_type in available_type:
                available_type.remove(neb_type)
        output_garden[i-1] = available_type[0]

    return output_garden


N = 4
paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
print(gardenNoAdj(N, paths))

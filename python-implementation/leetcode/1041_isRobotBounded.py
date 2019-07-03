def isRobotBounded(instructions: str) -> bool:
    start = [0,0]
    current_pos = start.copy()
    current_dir = "N"

    for i in range(0, 100):
        for index, step in enumerate(instructions):
            if step == "G":
                if current_dir == "N":
                    current_pos[1] += 1
                elif current_dir == "S":
                    current_pos[1] -= 1
                elif current_dir == "E":
                    current_pos[0] += 1
                elif current_dir == "W":
                    current_pos[0] -= 1
            elif step == "L":
                if current_dir == "N":
                    current_dir = 'W'
                elif current_dir == "S":
                    current_dir = 'E'
                elif current_dir == "E":
                    current_dir = 'N'
                elif current_dir == "W":
                    current_dir = 'S'
            elif step == "R":
                if current_dir == "N":
                    current_dir = 'E'
                elif current_dir == "S":
                    current_dir = 'W'
                elif current_dir == "E":
                    current_dir = 'S'
                elif current_dir == "W":
                    current_dir = 'N'
            if current_pos == start and index == len(instructions)-1:
                return True
    return False


asa = ["GGLLGG", "GG", "GL", "GLGLGGLGL"]
for a in asa:
    print(isRobotBounded(a))
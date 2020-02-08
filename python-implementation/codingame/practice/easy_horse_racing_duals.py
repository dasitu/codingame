import sys

n = int(input())
horses = []
for i in range(n):
    horses.append(int(input()))
horses.sort()

print(horses, file=sys.stderr)

closest = horses[0]
for index_1, leg_1 in enumerate(horses[:-1]):
    leg_2 = horses[index_1 + 1]
    diff = abs(leg_1 - leg_2)
    if diff < closest:
        closest = diff

    if closest == 0:
        break
print(closest)
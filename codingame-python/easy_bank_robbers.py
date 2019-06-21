import sys
import math

# robbers = int(input())
# vaults = int(input())

robbers = 4
vaults = 4
combine = ["3 2",
           "4 1",
           "7 6",
           "7 1"]

# robbers = 2
# vaults = 4
# combine = ["3 1",
#           "3 2",
#           "4 0",
#           "4 0"]


vaults_time = []
for i in range(vaults):
    # t_len, d_len = [int(j) for j in input().split()]
    t_len, d_len = [int(j) for j in combine[i].split()]
    spent_time = int(math.pow(10, d_len) * math.pow(5, t_len - d_len))
    vaults_time.append(spent_time)

print("vaults_time:{}".format(vaults_time), file=sys.stderr)

current_spent = [0] * robbers

# assign the initial value
i = 0
while i in range(robbers) and i in range(vaults):
    current_spent[i] = vaults_time[i]
    i += 1

if vaults > robbers:
    for v_time in vaults_time[robbers:]:
        current_spent.sort()
        current_spent[0] += v_time

print(sorted(current_spent)[-1])
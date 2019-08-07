a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]
n = int(input())
u = str(a) * b + str(c) * d

t = u
for i in range(n-1):
    f = t[-(b+d):]
    for s in f:
        t += str((int(s) + 1) % 10)
print(t)
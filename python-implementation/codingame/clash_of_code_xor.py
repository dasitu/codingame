s = input()
m = dict(zip(input(), [0,1]))
n = int(input())
f = 0
for i in range(n):
    l = input()
    for key in m.keys():
        l.replace(key, m[key])
    f = int(l,2) ^ f
print(f)
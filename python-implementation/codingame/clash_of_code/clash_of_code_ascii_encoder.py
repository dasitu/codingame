a, b = [int(i) for i in input().split()]
input()
e = input()
c = {" ": 26, ".": 27, ",": 28}
d = {26: " ", 27: ".", 28: ","}
t = ""
for i in e:
    i = c[i] if i in c.keys() else ord(i) - 65
    v = (a * i + b) % 29
    t += d[v] if v in d.keys() else chr(v + 65)
print(t)
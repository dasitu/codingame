s = 0
e = 100
for i in range(int(input())):
    l = input().split(" ")
    a = int(l[0])
    if "+" in l:
        s = max(a,s)
    if "-" in l:
        e = min(a,e)
    if "=" in l:
        print(a)
        exit(0)

if (e - s) != 2:
    print("Impossible")
else:
    print(e-1)
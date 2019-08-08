s = input().lower()
t = input().lower()
i = 0
for m in t.split(" "):
    if s in m:
        i += 1
print(i)

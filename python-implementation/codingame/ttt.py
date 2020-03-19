a = 121
b = "".join(reversed(str(a)))
c = str(a)[::-1]
print(b)
print(c)

if str(a) == str(a)[::-1]:
    print(1)

print(2)
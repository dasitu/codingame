m = int(input())
y = int(input())
r = 28
if y % 100 == 0 and y % 400 == 0:
    r = 29
elif y % 100 and y % 4 == 0:
    r = 29

d = 30
if (m <= 7 and m % 2) or (m > 7 and not m % 2):
    d += 1

print(d if m != 2 else r)

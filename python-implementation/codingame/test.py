# -*- coding: utf-8 -*-

import sys

a = [1, 3, 5, 7, 9]
print(a[0])
print(a[-1])
print(a[2:4])
end = ":"

print(end)
for v in a:
    print(v, end=" ", file=sys.stderr)

print("#######")
for v in a:
    print(v)

if "-h" in sys.argv:
    print("help")
elif "-V" in sys.argv:
    print("version")

print("中文")

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

for i in range(10,1,-2):
    print(i)
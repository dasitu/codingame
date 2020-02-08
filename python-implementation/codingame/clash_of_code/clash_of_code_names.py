max = int(input())
s_list = input().split(",")
n = int(input())
for i in range(n):
    str = input().split(",")
    if str[0] in s_list:
        max -= int(str[1])

if max >= 0:
    print("true")
    print(max)
else:
    print("false")
    print(max*-1)
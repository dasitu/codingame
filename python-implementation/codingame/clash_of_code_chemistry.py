m = {"1H4": "meth", "2H6": "eth", "3H8": "prop", "4H10": "but", "5H12": "pent"}
c = h = 0
for i in range(int(input())):
    l = input()
    c += l.count("C")
    h += l.count("H")
s = "{}H{}".format(c, h)
print(m[s] + "ane" if s in m.keys() else "NONE")

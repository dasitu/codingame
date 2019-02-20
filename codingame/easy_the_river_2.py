def cal_next(r: int) -> int:
    for d in str(r):
        r += int(d)
    return r


def river_2_bad(num):
    # num = int(input())
    found = "NO"
    all_possible = list(range(1, num + 1))

    for i in all_possible:
        print("trying:{}, all_possible count:{}".format(i, len(all_possible)))
        r_n = i
        while r_n < num:
            r_n = cal_next(r_n)
            if r_n == num:
                found = "YES"
                break
            elif r_n in all_possible:
                all_possible.remove(r_n)
    return found


def river_2(num):
    # num = int(input())
    found = "NO"
    d_len = len(str(num))
    possible = d_len * 9
    for i in range(1, possible):
        pre_num = num - i
        if cal_next(pre_num) == num:
            found = "YES"
            break
    return found


testcases = [(20, "NO"), (13, "YES"), (984, "NO"), (1006, "NO"), (9915, "YES"), (91004, "NO")]
for num, result in testcases:
    actual = river_2(num)
    print("num:{}, expect:{}, actual:{}".format(num, result, actual))

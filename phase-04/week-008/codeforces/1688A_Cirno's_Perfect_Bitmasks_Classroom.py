for _ in range(int(input())):
    num = int(input())
    res = num & -num  # finds the rightmost bit set to 1, hence th minimum solution
    while not (res & num) or not (res ^ num):
        res += 1

    print(res)

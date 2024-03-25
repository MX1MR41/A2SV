from math import ceil
t = int(input())
for _ in range(t):
    n, x = list(map(int,input().split()))
    arr = list(map(int, input().split()))
    MAX, MIN = 0, float('inf')
    for i in arr:
        num = ceil(x/i)
        if num > MAX:
            MAX = num
        if num < MIN:
            MIN = num
        print(MAX, MIN)
    teams = MAX - MIN
    # if teams > n:
    #     print(0)
    # else:
    #     print(teams)

    PRINT("\n\n")

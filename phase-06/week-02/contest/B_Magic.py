"""

PASSED

"""

for _ in range(int(input())):
    px = int(input())
    py = 100 - px

    y = lambda x: (100*x - px*x)/px
    eq = lambda x: 100*(x + y(x)) - px*(x + y(x))

    x = 1
    while True:
        ans = y(x)
        floored = int(ans)
        if floored == ans:
            break
        x += 1

    print(int(x + y(x)))


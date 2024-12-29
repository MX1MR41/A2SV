"""

PASSED

"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    tot = sum(a)

    if tot % 2 == 0:
        print(0)
        continue

    ans = float("inf")
    for x in a:
        temp = x
        ops = 0

        while (temp + x) % 2 == 0:
            temp //= 2
            ops += 1

        ans = min(ans, ops)

    print(ans)

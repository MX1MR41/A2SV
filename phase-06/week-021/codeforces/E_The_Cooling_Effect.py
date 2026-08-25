"""

https://codeforces.com/gym/591947/problem/E

"""

for _ in range(int(input())):
    input()
    n, a = list(map(int, input().split()))

    ns = list(map(int, input().split()))
    ns = [i - 1 for i in ns]
    airs = list(map(int, input().split()))

    c = {a: b for a, b in zip(ns, airs)}

    res = [float("inf")] * n

    pre_min = float("inf")
    for i in range(n):
        if i in c:
            pre_min = min(pre_min, c[i])

        res[i] = min(pre_min, res[i])
        pre_min += 1

    suff_min = float("inf")
    for i in range(n - 1, -1, -1):
        if i in c:
            suff_min = min(suff_min, c[i])

        res[i] = min(suff_min, res[i])
        suff_min += 1

    print(*res)

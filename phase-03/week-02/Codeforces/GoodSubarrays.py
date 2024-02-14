from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input()))
    res = 0
    pre = defaultdict(int)
    pre[0] += 1

    p = 0

    for i in range(n):
        p += arr[i]
        pre[p - i - 1] += 1
        res += pre[p - i - 1] - 1

    print(res)
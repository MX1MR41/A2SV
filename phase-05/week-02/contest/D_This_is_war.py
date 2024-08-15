"""
PASSED
"""

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    _max = max(arr)
    cnt = Counter(arr)
    arr = [(arr[i], i + 1) for i in range(n)]
    arr.sort()
    winners = set()

    p = 0
    prefix = []

    for x, i in arr:
        p += x
        prefix.append(p) 

    for i in reversed(range(n)):
        x, j = arr[i]
        if x >= _max or prefix[i] >= _max or cnt[x] * x >= _max:
            winners.add(j)
            continue

        if i < n - 1:
            y, k = arr[i+1]
            if (x >= y or prefix[i] >= y or cnt[x] * x >= y) and k in winners:
                winners.add(j)
                continue

    print(len(winners))
    print(*sorted(winners))

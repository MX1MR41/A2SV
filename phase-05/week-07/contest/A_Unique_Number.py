"""

https://codeforces.com/gym/549906/problem/A

PASSED
"""

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = Counter(arr)
    arr = [(i, ind+1) for ind, i in enumerate(arr)]

    arr.sort()
    for i, ind in arr:
        if cnt[i] == 1:
            print(ind)
            break
    else:
        print(-1)
"""

https://codeforces.com/gym/511242/problem/C

PASSED
"""

from bisect import bisect_right

s, b = list(map(int, input().split()))
arr = list(map(int, input().split()))
bases = []
for _ in range(b):
    bases.append(list(map(int, input().split())))

bases.sort()

pre = [0]
p = 0
for i in bases:
    p += i[1]
    pre.append(p)

pre.append(pre[-1])

defs = [i[0] for i in bases]

res = []

for ship in arr:
    ans = bisect_right(defs, ship)

    if ans == len(defs):
        res.append(pre[ans])
    elif defs[ans] > ship:
        res.append(pre[ans])
    else:
        res.append(pre[ans + 1])

print(*res)

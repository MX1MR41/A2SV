"""
https://codeforces.com/contest/1000/problem/C
"""

from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    l, r = list(map(int, input().split()))
    d[l] += 1
    d[r + 1] -= 1

s = sorted(d.items())

res = defaultdict(int)

pre = 0
for i in range(len(s) - 1):
    x, p = s[i]
    pre += p
    res[pre] += s[i + 1][0] - x


print(*[res[i] for i in range(1,n +1)])

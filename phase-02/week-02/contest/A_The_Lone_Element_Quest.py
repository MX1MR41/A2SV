"""

https://codeforces.com/gym/495129/problem/A

PASSED
"""
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    e = {x:ind for ind,x in enumerate(arr)}
    s = set(arr)
    q = Counter(arr)

    i = s.pop()
    if q[i] == 1:
        print(e[i]+1)
    else:
        j = s.pop()
        print(e[j]+1)
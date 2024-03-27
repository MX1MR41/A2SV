"""

https://codeforces.com/gym/513152/problem/B

PASSED
"""
from math import ceil
def check(wag, n, k, v, t):
    tot = 0
    
    for i in range(n):
        tot += ceil(v[i]/wag) * t[i]

    if tot > k:
        return False
    return True

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    v = list(map(int, input().split()))
    t = list(map(int, input().split()))
    l, r = 1, sum(v)
    ans = r
    while l <= r:
        mid = (l+r)//2

        if check(mid, n, k, v, t):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    
    if check(ans, n, k, v, t):
        print(ans)
    else:
        print(-1)

    


    
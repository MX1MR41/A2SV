from math import gcd
from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if a.count(a[0]) == n:
        print(0)
        continue
    
    flag = False
    for x in a:
        if (x >= k and a[0] <= k) or (x <= k and a[0] >= k):
            print(-1)
            flag = True
            break

    if flag: continue

    g = abs(k - a[0])
    for i in a:
        g = gcd(g, abs(k - i))

    ans = 0
    for i in a:
        ans += (abs(k - i) // g - 1)

    print(ans)


"""

https://codeforces.com/gym/499338/problem/B

PASSED
"""


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    s = input()
    l = 0
    res = float("inf")
    w = 0
    b = 0
    for r in range(n):
        if s[r] == "W":
            w += 1
        b += 1

        while l <= r and b >= k:
            res = min(res, w)
            ls = s[l]
            if ls == "W":
                w -= 1
            l += 1
            b -= 1

    print(res)


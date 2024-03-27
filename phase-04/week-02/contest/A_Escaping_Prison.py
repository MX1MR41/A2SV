"""

https://codeforces.com/gym/513152/problem/A

PASSED
"""

for _ in range(int(input())):
    n, h = list(map(int, input().split()))
    res = 0
    for _ in range(n):
        res += max(list(map(int, input().split())))

    if res >= h: print("YES")
    else: print("NO")
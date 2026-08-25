"""

https://codeforces.com/problemset/problem/448/D

"""

def check(mid, n, m):
    res = 0

    for i in range(1, n + 1):
        res += min(m, mid // i)

    return res >= k

n, m, k = map(int, input().split())

l, r = 1, n * m
res = r
while l <= r:
    mid = (l + r) // 2
    
    if check(mid, n, m):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
        
print(res)


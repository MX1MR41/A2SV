from math import comb

n, m, t = map(int, input().split())

ans = 0
for b in range(4, t):
    ans += comb(n, b)  * comb(m, t  - b)

print(ans)
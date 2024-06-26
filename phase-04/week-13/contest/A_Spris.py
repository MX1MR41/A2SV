"""

https://codeforces.com/gym/528792/problem/A

PASSED
"""

m, a, b = list(map(int, [input(), input(), input()]))

ans = 0
for i in range(m+1):
    if a >= 2*i and b >= 4*i:
        ans = i + 2*i + 4*i

    else: break

print(ans)
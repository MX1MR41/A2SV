"""

https://codeforces.com/gym/555219/problem/A

PASSED
"""

n, m = list(map(int, input().split()))

ans = []

for i in range(m):
    curr = n//(m-i)
    n -= curr
    ans.append(curr)

print(*ans)
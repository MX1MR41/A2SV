"""

https://codeforces.com/gym/495129/problem/B

PASSED
"""
n = t = int(input())
ans = 0
mat = []
for _ in range(t):
    mat.append(list(map(int,input().split())))

c = n//2
ans += sum(mat[c])

for i in range(n):
    if i == c:
        continue

    ans += mat[i][i]
    ans += mat[i][c]
    ans += mat[i][n -1 -i]

print(ans)


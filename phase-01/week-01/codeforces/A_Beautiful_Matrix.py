"""
https://codeforces.com/problemset/problem/263/A

PASSED
"""

rows = 5
cols = 5
mat = []
index = []

for i in range(rows):
    row = list(map(int, input().split()))
    mat.append(row)

for i in range(rows):
    for j in range(cols):
        if mat[i][j] == 1:
            index.append(i)
            index.append(j)

ans = (abs(index[0]-2) + abs(index[1]-2))
print(ans)



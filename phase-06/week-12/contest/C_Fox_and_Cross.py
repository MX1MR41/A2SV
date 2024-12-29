"""

PASSED

"""


from collections import defaultdict


n = int(input())

mat = []
for _ in range(n):
    mat.append(input())



dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
inbound = lambda i, j: 0 <= i < n and 0 <= j < n

crossed = defaultdict(bool)

def center(i, j):
    if crossed[(i, j)]:
        return False
    
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if mat[ni][nj] != "#" or crossed[(ni, nj)]:
            return False
        
    return True

def cross(i, j):
    crossed[(i, j)] = True
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        crossed[(ni, nj)] = True



for i in range(1, n - 1):
    for j in range(1, n - 1):
        if mat[i][j] == "#" and center(i, j):
            cross(i, j)

ans = True
for i in range(n):
    for j in range(n):
        if mat[i][j] == "#" and not crossed[(i, j)]:
            ans = False
            break

    if not ans:
        break

if ans:
    print("YES")
else:
    print("NO")
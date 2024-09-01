"""
https://codeforces.com/gym/545013/problem/C

PASSED
"""

from collections import defaultdict


n = int(input())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

# print(mat)

row, col = defaultdict(set), defaultdict(set)

for i in range(n):
    for j in range(n):
        row[i].add(mat[i][j])
        col[j].add(mat[i][j])

def valid(num, r, c):
    a, b = row[r], col[c]

    for i in a:
        if num - i in b:
            return True
    for i in b:
        if num - i in a:
            return True
        
    return False

for i in range(n):
    for j in range(n):
        if mat[i][j] != 1 and not valid(mat[i][j], i, j):
            print("No")
            exit()

print("Yes")


"""
https://codeforces.com/gym/491508/problem/B

PASSED
"""

n = int(input())

for _ in range(n):
    b = input()
    a = ""
    for i in range(0, len(b), 2):
        j = 0
        if i == len(b) - 2:
            a += b[i:]
        else:
            a += b[i:i+2][j]

    print(a)
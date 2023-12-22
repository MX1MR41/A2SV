"""
https://codeforces.com/gym/493037/problem/B

PASSED
"""

from math import ceil
n = int(input())

for _ in range(n):
    s = input()
    yes = "Yes" * (ceil(len(s)/3) + 2)

    if s in yes:
        print("YES")
    else:
        print("NO")
"""
https://codeforces.com/gym/493037/problem/C

PASSED
"""

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    SET = set()
    found = False

    for i in range(2, n - 1):

        SET.add(s[i - 2:i])
        if s[i:i+2] in SET:
            found = True
            break

    print("YES" if found else "NO")
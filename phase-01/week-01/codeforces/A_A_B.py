"""
https://codeforces.com/problemset/problem/1772/A

PASSED
"""

n = int(input())
for i in range(n):
    str = input()
    print(int(str[0]) + int(str[-1]))

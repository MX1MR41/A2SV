"""
https://codeforces.com/problemset/problem/758/A

PASSED
"""

n = int(input())
arr = list(map(int, input().split()))
total = 0
m = max(arr)
for i in arr:
    total += (m-i)

print(total)
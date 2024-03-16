"""
https://codeforces.com/gym/503628/problem/C

PASSED
"""

n = int(input())
arr = list(map(int,input().split()))

arr.sort()

pre = 0
res = 0

for i in range(n):
    j = arr[i]
    if pre <= j:
        res += 1
        pre += j
    else:
        continue



print(res)